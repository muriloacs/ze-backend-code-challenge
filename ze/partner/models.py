# -*- coding: utf-8 -*-

from django.contrib.gis.db import models

from .managers import PartnerQuerySet


class Partner(models.Model):
    trading_name = models.CharField(max_length=100, blank=False)
    owner_name = models.CharField(max_length=100, blank=False)
    document = models.CharField(max_length=50, blank=False, unique=True)
    coverage_area = models.MultiPolygonField(srid=4326, null=False, spatial_index=True)
    address = models.PointField(null=False, spatial_index=True)
    # Creates a spatial index for the given geometry field. Default is True, just making it explicit.

    objects = PartnerQuerySet.as_manager()

    def __str__(self):
        return self.trading_name
