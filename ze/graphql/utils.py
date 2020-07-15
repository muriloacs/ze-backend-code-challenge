# -*- coding: utf-8 -*-

from collections import namedtuple

from graphql_relay import from_global_id


def from_graphene_id(global_id):
    # https://github.com/graphql-python/graphene/issues/124#issuecomment-241823565
    Rid = namedtuple('Rid', 'name id')
    rid = Rid(*from_global_id(global_id))
    return rid.id
