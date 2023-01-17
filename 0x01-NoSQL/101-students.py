#!/usr/bin/env python3
"""
    A python function that returns all students sorted by average score
    the top must be ordered
    the avrerage score must be part of each item key = averageScore
"""


def top_students(mongo_collection):
    """
       return the average score 
    """
    return mongo_collection.aggregate([
        { "$project": {
            "name": "$name",
            "averageScore": { "$avg": "$topics.score"}
            } 
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])