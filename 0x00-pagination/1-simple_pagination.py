#!/usr/bin/env python3
""" Contains:
    - functions: index_range.
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

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
        """Return page of given number and size.
        """
        assert type(page) is int
        assert page > 0
        assert type(page_size) is int
        assert page_size > 0
        idx_first_item, idx_last_item = self.index_range(page, page_size)
        return self.dataset()[idx_first_item:idx_last_item]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Return tuple of index of first item in given page, and index
        of its last item
        """
        return ((page - 1) * page_size, page * page_size)
