#!/usr/bin/env python3
""" function to return tuple of size two
with start index and end index corresponding
to range of indexes to return in a list for
a particular pagination parameters """


def index_range(page, page_size):
    """ index_range function """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
