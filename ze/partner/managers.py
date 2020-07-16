# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from django.contrib.gis.db.models.functions import Distance


class PartnerQuerySet(models.QuerySet):

    def search_nearest_from_location(self, location):
        return self.filter(coverage_area__intersects=location).annotate(
            distance=Distance('address', location)).earliest('distance')
