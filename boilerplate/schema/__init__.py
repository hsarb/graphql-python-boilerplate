import graphene

from graphene_sqlalchemy import SQLAlchemyConnectionField
from boilerplate.schema.User import Users, Query as UserQuery, Mutations as UserMutations


class Query(UserQuery, graphene.ObjectType):
    pass


class Mutations(UserMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations, types=[Users])
