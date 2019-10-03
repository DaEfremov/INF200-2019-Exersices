# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov'
__email__ = 'daniil.vitalevich.efremov@nmbu.no'


import pytest


def median(data):
    sort_data = sorted(data)
    num_el = len(sort_data)

    if data == []:
        raise ValueError

    if num_el % 2 == 1:
        return sort_data[num_el // 2]
    else:
        return (sort_data[num_el // 2 - 1] + sort_data[num_el // 2]) / 2


def test_median_of_singleton():
    assert median([4]) == 4


def test_median_of_list_with_odd_number():
    odd_list = [1, 2, 3]

    assert median(odd_list) == 2


def test_median_of_list_with_even_number():
    even_list = [2, 4]

    assert median(even_list) == 3


def test_median_of_ordered_list():
    ordered_list = [1, 2, 3, 4, 5]

    assert median(ordered_list) == 3


def test_median_of_reverse_ordered_list():
    reverse_ordered_list = [5, 4, 3, 2, 1]

    assert median(reverse_ordered_list) == 3


def test_median_of_unordered_list():
    unordered_list = [1, 5, 3, 4, 2]

    assert median(unordered_list) == 3


def test_median_raises_value_error_on_empty_list():
    with pytest.raises(ValueError):
        median([])
