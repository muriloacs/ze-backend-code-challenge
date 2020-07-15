# -*- coding: utf-8 -*-

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

from graphene import ObjectType, Field, ID
from graphene_django.filter import DjangoFilterConnectionField

from ...partner.models import Partner
from ..utils import from_graphene_id
from .inputs import LocationInput
from .types import PartnerType


class PartnerQuery(ObjectType):
    partner = Field(PartnerType, id=ID(), location=LocationInput())
    all_partners = DjangoFilterConnectionField(PartnerType)

    def resolve_partner(self, info, **kwargs):  # noqa
        partner_id = kwargs.get('id')
        location = kwargs.get('location')

        if partner_id:
            return Partner.objects.get(pk=from_graphene_id(partner_id))

        if location:
            user_location = Point((location['lat'], location['long']))
            return Partner.objects.filter(coverage_area__intersects=user_location).annotate(
                distance=Distance('address', user_location)).earliest('distance')
