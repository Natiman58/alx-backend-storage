#!/usr/bin/env python3
"""
    A redis module that writes strings to reddis
"""
from typing import Optional, Union
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
            A method that stores the data into redis cache using key
            returns the string format of the key used to set the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    
    def get(self, key: str, fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
        """
            A method to get data from redis cache
        """
        data = self._redis.get(key)

        if data and fn and callable:
            return fn(data)
        return data


    def get_str(self, rr_data: str) -> str:
        """
            returns the string form of a data(encoded bytes)
            that is returned from redis
            rr_data: the redis return data
        """
        return rr_data.decode('utf-8', 'strict')
    
    def get_int(self, rr_data: str):
        """
            returns the int form of the returned byte form data from redis
        """
        return int(rr_data)
