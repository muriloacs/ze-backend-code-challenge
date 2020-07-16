# -*- coding: utf-8 -*-

from django.contrib.gis.geos import Point
from django.db import IntegrityError
from django.test import TestCase

from model_mommy import mommy

from ..models import Partner
from ..utils import load_partner_test_data


class PartnerTestCase(TestCase):

    def setUp(self):
        self.partners = [partner for partner in load_partner_test_data()]

    def test_partner_not_found_for_point(self):
        point = Point((-46.13451, -1.356126))  # this point isn't nearby any partner
        self.assertFalse(Partner.objects.filter(coverage_area__contains=point).exists())

    def test_partner_found_for_point(self):
        point = Point((-38.59825, -3.774185))  # this point is nearby partner with id 3
        self.assertTrue(Partner.objects.filter(coverage_area__contains=point).exists())
        self.assertEquals(Partner.objects.get(coverage_area__intersects=point).document, self.partners[2].document)

    def test_nearest_partner_from_location(self):
        point = Point((-46.66770, -23.659360))  # this point is nearby 2 partners ids 9 and 29, but nearest to 9
        partner_documents = Partner.objects.filter(coverage_area__intersects=point).values_list('document', flat=True)
        self.assertGreater(partner_documents.count(), 1)
        self.assertIn(self.partners[8].document, partner_documents)
        self.assertIn(self.partners[28].document, partner_documents)
        self.assertEquals(Partner.objects.search_nearest_from_location(point).document, self.partners[8].document)

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
