#!/usr/bin/env python3
""" Script containing the FIFO caching class """

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ Docstring for the FIFOCache class """
    def __init__(self):
        """ Inintiation class for FIFOCache class """
        super().__init__()

    def put(self, key, item):
        """ Method for adding new items in the cache data dictionary """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                keys = list(self.cache_data.keys())
                print(f"DISCARD: {keys[0]}")
                del self.cache_data[keys[0]]
            self.cache_data[key] = item

    def get(self, key):
        """ Method for retriving data with relation with the keys in
        cache data """
        return self.cache_data.get(key)
