#!/usr/bin/env python3
""" Contains:
    - functions: index_range.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return tuple of index of first item in given page, and index
    of its last item
    """
    return ((page - 1) * page_size, page * page_size)
