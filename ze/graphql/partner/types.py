# -*- coding: utf-8 -*-

from graphene import relay
from graphql_geojson import GeoJSONType

from ze.partner.models import Partner


class PartnerType(GeoJSONType):

    class Meta:
        model = Partner
        filter_fields = ['id']
        interfaces = (relay.Node, )
        fields = ('trading_name', 'owner_name', 'document', 'coverage_area')
        geojson_field = 'coverage_area'
