# -*- coding: utf-8 -*-

import os
import json

from django.conf import settings
from django.contrib.gis.geos import Point, Polygon, MultiPolygon

from model_mommy import mommy

from .models import Partner


def load_partner_test_data():
    pdvs_file_path = os.path.join(settings.BASE_DIR, 'partner/tests/files/pdvs.json')
    with open(pdvs_file_path, 'r') as f:
        pdvs_json = json.loads(f.read())

    for pdv in pdvs_json['pdvs']:
        poligons = [Polygon(polygon[0]) for polygon in pdv['coverageArea']['coordinates']]
        coverage_area = MultiPolygon(*poligons)
        address = Point(pdv['address']['coordinates'])
        yield mommy.make(Partner,
                         trading_name=pdv['tradingName'],
                         owner_name=pdv['ownerName'],
                         document=pdv['document'],
                         coverage_area=coverage_area,
                         address=address)
