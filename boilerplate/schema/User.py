import graphene

from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from boilerplate.database import db_session
from boilerplate.models.User import User as UserModel


class UserAttributes:
    firstName = graphene.String()
    lastName = graphene.String()
    email = graphene.String()
    password = graphene.String()


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()

    # User Query
    user = graphene.relay.Node.Field(User)
    users = SQLAlchemyConnectionField(User)


class UserInput(graphene.InputObjectType, UserAttributes):
    pass


class CreateUser(graphene.Mutation):
    ok = graphene.Boolean()
    user = graphene.Field(lambda: User)

    class Arguments:
        input = UserInput(required=True)

    def mutate(self, info, user):
        user = UserModel(**input)

        db_session.add(user)
        db_session.commit()
        ok = True

        return CreateUser(user=user, ok=ok)


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
