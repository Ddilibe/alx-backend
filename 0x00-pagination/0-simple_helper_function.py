#!/usr/bin/env python3
""" Script that does the simple helper function task """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Function that accepts two arguments and returns an integer

        Args:
            :params page [int] - The first argument
            :params page_size [int] - The second argument

        Return:
            This function returns a tuple
    """
    return ((page*page_size) - page_size, (page*page_size))
