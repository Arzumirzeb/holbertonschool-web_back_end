#!/usr/bin/env python3
"""Python func that inserts a new document in a collection based on kwargs"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert school"""
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
