# -*- coding: utf-8 -*-

from collections import namedtuple

from graphql_relay import from_global_id


def from_graphene_id(global_id):
    """
    Returns model row id from graphene global id.
    :param global_id:
    :return:
    """
    Rid = namedtuple('Rid', 'name id')
    rid = Rid(*from_global_id(global_id))
    return rid.id
