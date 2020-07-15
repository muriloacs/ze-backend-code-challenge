# -*- coding: utf-8 -*-

from graphene import relay
from graphene_django.types import DjangoObjectType
from graphql_geojson import converter  # noqa

from ...partner.models import Partner


class PartnerType(DjangoObjectType):

    class Meta:
        model = Partner
        filter_fields = ['id']
        interfaces = (relay.Node, )
