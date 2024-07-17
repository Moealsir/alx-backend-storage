#!/usr/bin/env python3
"""Redis exercise"""
from functools import wraps
import redis
from typing import Any, Callable, Union
import uuid


class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
