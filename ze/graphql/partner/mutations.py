# -*- coding: utf-8 -*-

from graphene import Boolean, Field, Mutation, String

from ze.partner.models import Partner
from .types import PartnerType


class PartnerMutation(Mutation):
    success = Boolean()
    partner = Field(PartnerType)

    class Arguments:
        trading_name = String(required=True)
        owner_name = String(required=True)
        document = String(required=True)

    def mutate(self, info, **kwargs):
        try:
            partner = Partner.objects.create(trading_name=kwargs.get('trading_name'),
                                             owner_name=kwargs.get('owner_name'),
                                             document=kwargs.get('document'),
                                             coverage_area=kwargs.get('coverage_area'),
                                             address=kwargs.get('address'))
            success = True
        except Exception as e:
            partner = None
            success = False

        return PartnerMutation(success=success, partner=partner)
