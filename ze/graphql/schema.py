# -*- coding: utf-8 -*-

import graphene
from graphene_django.debug import DjangoDebug


# class Query(
#     ApplicationSettingsQuery,
#     graphene.ObjectType
# ):
#
#     debug = graphene.Field(DjangoDebug, name='__debug')
#
#
# class Mutation(graphene.ObjectType):
#     create_a_link = CreateALinkMutation.Field()
#
#
# schema = graphene.Schema(query=Query, mutation=Mutation)
