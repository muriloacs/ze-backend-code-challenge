# -*- coding: utf-8 -*-

from graphene import ObjectType, relay
from graphene_django.filter import DjangoFilterConnectionField

from .types import PartnerType


class PartnerQuery(ObjectType):
    partner = relay.Node.Field(PartnerType)
    all_partners = DjangoFilterConnectionField(PartnerType)
