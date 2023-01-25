#!/usr/bin/env python3
""" Script containing the basic dictionary Class """

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """docstring for BaseCache"""
    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
            Method for updating the cache data.
            It accepts a key value and updates the cache data
            with the item and key as the reference

            Args:
                :param @key [Any] - The first argument
                :param @item [Any] - The second argument

            Return:
                No return value
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Method for getting a value form cache data """
        return self.cache_data.get(key)
