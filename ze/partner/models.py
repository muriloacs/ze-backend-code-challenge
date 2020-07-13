# -*- coding: utf-8 -*-

from django.db import models


class Partner(models.Model):
    tradingName = models.CharField(max_length=100)
    ownerName = models.CharField(max_length=100)
    document = models.CharField(max_length=100, unique=True)
