"""
    A python function that lists all docs in a collection
"""
import pymongo


def list_all(mongo_collection):
    if mongo_collection == None:
        return []
    col_list = list(mongo_collection.find())
    return col_list

