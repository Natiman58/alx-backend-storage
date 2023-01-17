#!/usr/bin/env python3
"""
    A python function that lists all of school collection
    having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    return mongo_collection.find({"topics": topic})
