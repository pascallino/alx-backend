#!/usr/bin/env python3
""" Write a function named index_range that takes
two integer arguments page and page_size. """


def index_range(page: int, page_size: int) -> tuple:
    """ index range Page numbers are 1-indexed,
    i.e. the first page is page 1."""
    if page <= 0 or page_size <= 0:
        return 0, 0
    startindex = (page - 1) * page_size
    endindex = startindex + page_size
    return startindex, endindex
