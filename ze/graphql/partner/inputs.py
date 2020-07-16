# -*- coding: utf-8 -*-

from graphene import Field, Float, InputObjectType, String
from graphene.types.generic import GenericScalar


class LocationInput(InputObjectType):
    lat = Field(Float, required=True)
    long = Field(Float, required=True)


class GeometryInput(InputObjectType):
    type = String()
    coordinates = GenericScalar()


class PartnerInput(InputObjectType):
    trading_name = Field(String, required=True)
    owner_name = Field(String, required=True)
    document = Field(String, required=True)
    coverage_area = GeometryInput(required=True)
    address = GeometryInput(required=True)
