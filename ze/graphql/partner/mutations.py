# -*- coding: utf-8 -*-

import logging

from graphene import Field, Mutation
from graphql import GraphQLError  # noqa
from graphql_geojson import Geometry

from .inputs import PartnerInput
from .types import PartnerType
from ze.partner.models import Partner

logger = logging.getLogger(__name__)


class PartnerMutation(Mutation):
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
            return cls(partner=partner)
        except Exception as e:
            msg = 'Could not create partner due to: {}'.format(e)
            logger.error(msg)
            raise GraphQLError(msg)
