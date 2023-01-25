#!/usr/bin/env python3
""" Script containing the LIFO caching class """

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ Docstring for the LIFOCache class """
    def __init__(self):
        """ Inintiation class for LIFOCache class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Method for adding new items in the cache data dictionary """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
              and key not in self.cache_data.keys():
                print(f"DISCARD: {self.order[BaseCaching.MAX_ITEMS - 1]}")
                del self.cache_data[self.order[BaseCaching.MAX_ITEMS - 1]]
                self.order.pop()
            if key in self.cache_data.keys():
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Method for retriving data with relation with the keys in cache
        data """
        return self.cache_data.get(key)
