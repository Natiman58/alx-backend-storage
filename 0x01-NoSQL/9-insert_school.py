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
    added = []
    for k, v in kwargs.items():
        added = mongo_collection.insert({k: v})
    return added
