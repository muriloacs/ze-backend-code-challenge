# -*- coding: utf-8 -*-

from django.contrib.gis.db import models


class Partner(models.Model):
    trading_name = models.CharField(max_length=100, blank=False, null=False)
    owner_name = models.CharField(max_length=100, blank=False, null=False)
    document = models.CharField(max_length=100, blank=False, null=False, unique=True)
    coverage_area = models.MultiPolygonField(srid=4326, null=False)
    address = models.PointField(null=False)

    def __str__(self):
        return self.trading_name
