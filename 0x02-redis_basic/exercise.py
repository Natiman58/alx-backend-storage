#!/usr/bin/env python3
"""
    A redis module that writes strings to reddis
"""
from typing import Union
import uuid
import redis


class Cache:
    """
        A class to handle redis operations
    """
    def __init__(self):
        """
            store the instance of Redis client
            as a private variable; _redis
            and flush all the instances
        """
        self._redis = redis.Redis()  # create & store the redis client
        self._redis.flushdb()  # Delete all keys in the current db

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            A method that stores the data into redis as key val pairs
            returns the string format of the key used to set the data
        """
        key = int(uuid.uuid4())
        self._redis.set(key, data)

        return key
