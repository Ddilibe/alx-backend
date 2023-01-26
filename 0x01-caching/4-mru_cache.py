#!/usr/bin/env python3
""" Script containing the LIFO caching class """

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ Docstring for the MRUCache class """
    def __init__(self):
        """ Inintiation class for MRUCache class """
        super().__init__()
        self.order = {}

    def put(self, key, item):
        """ Method for adding new items in the cache data dictionary """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
              and key not in self.cache_data.keys():
                keys = sorted(self.order)
                print(f"DISCARD: {keys[len(keys)-1]}")
                del self.cache_data[keys[len(keys)-1]]
                del self.order[keys[len(keys)-1]]
            if key in self.cache_data.keys():
                self.order[key] += 1
            self.cache_data[key] = item
            self.order[key] = 0

    def get(self, key):
        """ Method for retriving data with relation with the keys in cache
        data """
        if key in self.order:
            self.order[key] += 1
        return self.cache_data.get(key)
