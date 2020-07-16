# -*- coding: utf-8 -*-

import json

from graphene_django.utils.testing import GraphQLTestCase
from graphql_relay import to_global_id

from ..utils import load_partner_test_data
from ze.graphql.schema import schema
from ze.graphql.partner.types import PartnerType


class PartnerTestCase(GraphQLTestCase):

    GRAPHQL_SCHEMA = schema

    def setUp(self):
        self.partners = [partner for partner in load_partner_test_data()]

    def assertFields(self, result, partner, partner_global_id):
        result_content = result.data['partner']
        self.assertEquals(result_content['id'], partner_global_id)
        self.assertEquals(result_content['tradingName'], partner.trading_name)
        self.assertEquals(result_content['ownerName'], partner.owner_name)
        self.assertEquals(result_content['document'], partner.document)
        self.assertEquals(result_content['coverageArea'], json.loads(partner.coverage_area.geojson))
        self.assertEquals(result_content['address'], json.loads(partner.address.geojson))

    def test_query_get_partner_by_id(self):
        partner = self.partners[0]
        partner_global_id = to_global_id(PartnerType._meta.name, partner.id)
        result = self.GRAPHQL_SCHEMA.execute(
            '''
            query partner($id: ID!){
                partner(id: $id) {
                    id
                    tradingName
                    ownerName
                    document
                    coverageArea {
                      type
                      coordinates
                    }
                    address {
                      type
                      coordinates
                    }
                }
            }
            ''',
            variables={'id': partner_global_id}
        )
        self.assertFields(result, partner, partner_global_id)

    def test_query_search_partner_by_location(self):
        partner = self.partners[2]
        partner_global_id = to_global_id(PartnerType._meta.name, partner.id)
        result = self.GRAPHQL_SCHEMA.execute(
            '''
            query partner($location: LocationInput!){
                partner(location: $location) {
                    id
                    tradingName
                    ownerName
                    document
                    coverageArea {
                      type
                      coordinates
                    }
                    address {
                      type
                      coordinates
                    }
                }
            }
            ''',
            variables={'location': {'lat': -38.59825, 'long': -3.774185}}
        )
        self.assertFields(result, partner, partner_global_id)

    def test_mutation_create_partner(self):
        trading_name = 'foo'
        owner_name = 'bar'
        document = '900XP800SP'
        coverage_area = {'type': 'MultiPolygon', 'coordinates': [[[[30, 20], [45, 40], [10, 40], [30, 20]]]]}
        address = {'type': 'Point', 'coordinates': [-46.57421, -21.785741]}

        result = self.GRAPHQL_SCHEMA.execute(
            '''
            mutation partner($input: PartnerInput!) {
                partner(input: $input) {
                    partner {
                        id
                        tradingName
                        ownerName
                        document
                        coverageArea {
                            type
                            coordinates
                        }
                        address {
                            type
                            coordinates
                        }
                    }
                }
            }
            ''',
            variables={'input': {
                'tradingName': trading_name,
                'ownerName': owner_name,
                'document': document,
                'coverageArea': coverage_area,
                'address': address
            }}
        )

        result_content = result.data['partner']['partner']
        self.assertEquals(result_content['tradingName'], trading_name)
        self.assertEquals(result_content['ownerName'], owner_name)
        self.assertEquals(result_content['document'], document)
        self.assertEquals(result_content['coverageArea'], coverage_area)
        self.assertEquals(result_content['address'], address)
