# -*- coding: utf-8 -*-

import os
import json

from django.conf import settings
from django.contrib.gis.geos import Point, Polygon, MultiPolygon
from django.db import IntegrityError
from django.test import TestCase

from model_mommy import mommy

from ..models import Partner


class PartnerTestCase(TestCase):

    partners = []

    def setUp(self):
        pdvs_file_path = os.path.join(settings.BASE_DIR, 'partner/tests/files/pdvs.json')
        with open(pdvs_file_path, 'r') as f:
            pdvs_json = json.loads(f.read())

        for pdv in pdvs_json['pdvs']:
            poligons = [Polygon(polygon[0]) for polygon in pdv['coverageArea']['coordinates']]
            coverage_area = MultiPolygon(*poligons)
            address = Point(pdv['address']['coordinates'])
            self.partners.append(mommy.make(Partner,
                                            trading_name=pdv['tradingName'],
                                            owner_name=pdv['ownerName'],
                                            document=pdv['document'],
                                            coverage_area=coverage_area,
                                            address=address))

    def test_partner_not_found_for_point(self):
        point = Point((-46.13451, -1.356126))  # this place isn't nearby any partner
        self.assertFalse(Partner.objects.filter(coverage_area__contains=point).exists())

    def test_partner_found_for_point(self):
        point = Point((-38.59825, -3.774185))  # this place is nearby partner with id 3
        self.assertTrue(Partner.objects.filter(coverage_area__contains=point).exists())
        self.assertEquals(Partner.objects.get(coverage_area__intersects=point).document, self.partners[2].document)

    def test_document_must_be_unique(self):
        with self.assertRaises(IntegrityError):
            mommy.make(Partner,
                       trading_name='Foo',
                       owner_name='Bar',
                       document=self.partners[1].document)  # partner with such document already exists in the db

    def test_id_must_be_unique(self):
        with self.assertRaises(IntegrityError):
            partner = Partner(pk=self.partners[0].pk,  # partner with such id already exists in the db
                              trading_name='Foo',
                              owner_name='Bar',
                              document='35908711500')
            partner.save(force_insert=True)
