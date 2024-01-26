#!/usr/bin/env python3
""" Write a function named index_range that takes
two integer arguments page and page_size. """
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ index range Page numbers are 1-indexed,
    i.e. the first page is page 1."""
    if page <= 0 or page_size <= 0:
        return 0, 0
    startindex = (page - 1) * page_size
    endindex = startindex + page_size
    return startindex, endindex


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
        """ get page data"""
        assert isinstance(page, int) and page > 0,\
            "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0,\
            "Page size must be a positive integer"
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        if page < 1 or page > total_pages:
            return []

        start_index, end_index = index_range(page, page_size)
        return self.__dataset[start_index:end_index]
