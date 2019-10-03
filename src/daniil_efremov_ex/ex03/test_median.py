# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov'
__email__ = 'daniil.vitalevich.efremov@nmbu.no'


import pytest


def median(data):
    sort_data = sorted(data)
    num_el = len(sort_data)

    if num_el % 2 == 1:
        return sort_data[num_el // 2]
    else:
        return (sort_data[num_el // 2 - 1] + sort_data[num_el // 2]) / 2


def test_median_of_singleton():
    assert median([4]) == 4


def test_median_of_list_with_odd_number():
    odd_list = [1, 2, 3]

    assert median(odd_list) == 2
