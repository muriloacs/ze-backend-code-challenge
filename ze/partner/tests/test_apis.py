# -*- coding: utf-8 -*-

import json

from graphene_django.utils.testing import GraphQLTestCase

from ze.graphql.schema import schema
from ..utils import load_partner_test_data


class PartnerTestCase(GraphQLTestCase):

    GRAPHQL_SCHEMA = schema

    def setUp(self):
        self.partners = [partner for partner in load_partner_test_data()]

    def assert_response(self, response, fields):
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        for key, value in fields.items():
            self.assertEquals(content[key], value)

    def test_query_get_partner_by_id(self):
        partner = self.partners[0]

        response = self.query(
            '''
            query partner($id: Int!){
                partner(id: $id) {
                    id
                    trading_name
                    owner_name
                    document
                    coverage_area
                    address
                }
            }
            ''',
            op_name='partner',
            variables={'id': partner['id']}
        )

        self.assert_response(response, fields={
            'id': partner['id'],
            'trading_name': partner['trading_name'],
            'owner_name': partner['owner_name'],
            'document': partner['document'],
            'coverage_area': partner['coverage_area'],
            'address': partner['address'],
        })

    def test_query_search_partner_by_location(self):
        partner = self.partners[2]

        response = self.query(
            '''
            query partner($location: LocationInput!){
                partner(location: $location) {
                    id
                    trading_name
                    owner_name
                    document
                    coverage_area
                    address
                }
            }
            ''',
            op_name='partner',
            input_data={'lat': '-38.59825', 'long': '-3.774185'}
        )

        self.assert_response(response, fields={
            'id': partner['id'],
            'trading_name': partner['trading_name'],
            'owner_name': partner['owner_name'],
            'document': partner['document'],
            'coverage_area': partner['coverage_area'],
            'address': partner['address'],
        })

    def test_mutation_create_partner(self):
        trading_name = 'foo'
        owner_name = 'bar'
        document = '900XP800SP'
        coverage_area = [[[[30, 20], [45, 40], [10, 40], [30, 20]]]]
        address = [-46.57421, -21.785741]

        response = self.query(
            '''
            mutation partner($partnerInput: PartnerInput!) {
                partner(partnerInput: $partnerInput) {
                    partner {
                        id
                        trading_name
                        owner_name
                        document
                        coverage_area
                        address
                    }
                }
            }
            ''',
            op_name='partner',
            input_data={'trading_name': trading_name, 'owner_name': owner_name, 'document': document,
                        'coverage_area': coverage_area, 'address': address}
        )

        self.assert_response(response, fields={
            'trading_name': trading_name,
            'owner_name': owner_name,
            'document': document,
            'coverage_area': coverage_area,
            'address': address,
        })
