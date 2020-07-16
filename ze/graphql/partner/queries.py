# -*- coding: utf-8 -*-

import logging

from django.contrib.gis.geos import Point

from graphene import ObjectType, Field, ID
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLError  # noqa

from ..utils import from_graphene_id
from .inputs import LocationInput
from .types import PartnerType
from ze.partner.models import Partner

logger = logging.getLogger(__name__)


class PartnerQuery(ObjectType):
    partner = Field(PartnerType, id=ID(), location=LocationInput())
    all_partners = DjangoFilterConnectionField(PartnerType)

    def resolve_partner(self, info, **kwargs):  # noqa
        partner_id = kwargs.get('id')
        location = kwargs.get('location')

        if partner_id:
            try:
                return Partner.objects.get(pk=from_graphene_id(partner_id))
            except Exception:
                msg = 'Could not find any partner with id {}'.format(str(partner_id))
                logger.error(msg)
                raise GraphQLError(msg)

        if location:
            point = Point((location['lat'], location['long']))
            return Partner.objects.search_nearest_from_location(location=point)
