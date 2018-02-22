import graphene
import logging

from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from boilerplate.database import db_session
from boilerplate.models.User import User as UserModel

logger = logging.getLogger(__name__)


class Users(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    # User Query
    user = SQLAlchemyConnectionField(Users)
    users = SQLAlchemyConnectionField(Users)

    def resolve_user(self, info, id):
        query = Users.get(id=id)

        return query

    def resolve_users(self, info):
        query = Users.get_query(info)

        return query.all()


class UserInput(graphene.InputObjectType):
    id = graphene.String()
    firstName = graphene.String()
    lastName = graphene.String()
    email = graphene.String()
    password = graphene.String()


class CreateUser(graphene.Mutation):
    class Arguments:
        user_data = UserInput()

    ok = graphene.Boolean()
    user = graphene.Field(Users)

    @staticmethod
    def mutate(root, info, user_data=None):

        user = UserModel(
            firstName=user_data.firstName,
            lastName=user_data.lastName,
            email=user_data.email,
            password=user_data.password
        )

        db_session.add(user)
        db_session.commit()
        ok = True

        return CreateUser(user=user, ok=ok)


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
