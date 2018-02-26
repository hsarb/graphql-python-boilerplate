import graphene

from graphene_sqlalchemy import SQLAlchemyConnectionField
from boilerplate.schema.User import Query as UserQuery, Mutations as UserMutations


class Query(UserQuery, graphene.ObjectType):
    pass


class Mutations(UserMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
