# -*- coding: utf-8 -*-

from django.contrib.gis import admin

from .models import Partner

admin.site.register(Partner, admin.OSMGeoAdmin)
