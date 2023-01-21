#!/usr/bin/env python3
""" Script that does the simple helper function task """
import csv
import math
from typing import List, Tuple, Dict


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
            self.__dataset = dataset[1:]

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
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        value, j = index_range(page, page_size), self.__dataset
        return [j[i] for i in range(value[0], value[1]) if i < len(j)]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            Function to get the hyper version of this pagnination project

            Args:
                :params @page [int] - The first argument
                :params @page_size [int] - The second argument

            Return:
                This function returns a dictionary instance
        """
        value, ans = index_range(page, page_size), {}
        ans["page"], ans["page_size"], j = page, page_size, self.__dataset
        ans["data"] = self.get_page(page, page_size)
        ans["next_page"] = page + 1 if page+1 <= len(j)/page_size else None
        ans["prev_page"] = page - 1 if page-1 > 0 and page < (len(j)) else None
        ans["total_pages"] = math.ceil(len(self.__dataset)/page_size)
        return ans


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
