#!/usr/bin/env python3
""" Simple pagination module
This module contains Python code that illustrates the application
of pagination to retrieve information from a given dataset
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ __init__ method
        Instantiates the required variables """
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

    def index_range(self, page, page_size):
        """ index_range method
        Returns a tuple of size two containing a start index
        and an end index corresponding to the range of indexes
        to return in a list for those particular pagination parameters
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get_page method
        Returns items in a dataset based on the index range provided.
        It takes two integer arguments with page set to default value
        of 1 and page_size det to default value of 10
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0 and page_size > 0

        dataset = self.dataset()
        start_index, end_index = self.index_range(page, page_size)
        if start_index > len(dataset) or end_index > len(dataset):
            return []
        else:
            return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ get_hyper method
        Returns a dictionary containing certain keys based on the get_page
        method with usage of the same arguments as the get_page method
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
