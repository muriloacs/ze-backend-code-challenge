# -*- coding: utf-8 -*-

from graphene import Boolean, Field, Mutation
from graphql_geojson import Geometry

from .inputs import PartnerInput
from .types import PartnerType
from ze.partner.models import Partner


class PartnerMutation(Mutation):
    success = Boolean()
    partner = Field(PartnerType)

    class Arguments:
        input = PartnerInput(required=True)

    @classmethod
    def mutate(cls, root, info, input):  # noqa
        try:
            partner_data = input.__dict__
            partner_data.update({'coverage_area': Geometry.parse_value(partner_data['coverage_area'])})
            partner_data.update({'address': Geometry.parse_value(partner_data['address'])})
            partner = Partner.objects.create(**partner_data)
            success = True
        except Exception:  # noqa
            partner = None
            success = False

        return cls(success=success, partner=partner)
