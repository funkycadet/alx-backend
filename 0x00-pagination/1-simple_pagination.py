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
