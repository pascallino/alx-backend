#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Create a class BasicCache that
    inherits from BaseCaching and is a caching system:"""
    def __init__(self):
        """ init def function"""
        super().__init__()

    def put(self, key, item):
        """add items to dict"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get items from dict"""
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
