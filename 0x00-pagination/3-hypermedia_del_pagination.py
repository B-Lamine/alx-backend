#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        data = self.indexed_dataset()
        assert index >= 0 and index < len(data)
        undeleted_data = {
                k: data.get(k)
                for k in range(index, len(data))
                if data.get(k)
                }
        page = {
                k: v
                for k, v, _ in zip(undeleted_data.keys(),
                                   undeleted_data.values(),
                                   range(page_size + 1))
                }
        current_page = list(page.values())[:-1]
        next_index = list(page.keys())[-1]
        return {
                "index": index,
                "next_index": next_index,
                "page_size": len(current_page),
                "data": current_page
        }
