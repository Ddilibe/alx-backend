#!/usr/bin/env python3
""" Script that does the simple helper function task """
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.dataset()

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[0:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            """
                Method for getting page

                Args:
                    :params @page [int] - The first argument
                    :params @page_size [int] - The second argument

                Returns:
                    This function returns a list of list
            """
            for i in [page, page_size]:
                if type(i) != int :
                    raise AssertionError
                if i < 1:
                    raise AssertionError
            value = index_range(page, page_size)
            check = lambda x : self.__dataset[x] if x < len(self.__dataset) else pass
            return [check(i) for i in range(value[0], value[1])]

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
