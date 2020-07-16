# -*- coding: utf-8 -*-

from graphene import Field, ObjectType, Schema
from graphene_django.debug import DjangoDebug

from .partner.mutations import PartnerMutation
from .partner.queries import PartnerQuery


class Query(
    PartnerQuery,
    ObjectType
):
    debug = Field(DjangoDebug, name='__debug')


class Mutation(ObjectType):
    partner = PartnerMutation.Field()


schema = Schema(query=Query, mutation=Mutation)
