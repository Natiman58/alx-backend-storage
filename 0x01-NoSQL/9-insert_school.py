#!/usr/bin/env python3
"""
    A python function that inserts a new documnet in a collection
    based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
        insert a new doc in a collection
    """
    return mongo_collection.insert_one(kwargs).inserted_id
