# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov'
__email__ = 'daniil.vitalevich.efremov@nmbu.no'


def bubble_sort(some_data):
    dat = list(some_data)
    num_of_steps = len(dat) - 1

    for i in range(num_of_steps):

        for j in range(num_of_steps - i):
            if dat[j] > dat[j + 1]:
                dat[j], dat[j + 1] = dat[j + 1], dat[j]

    return dat


def test_empty():
    """Test that the sorting function works for empty list"""

    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""

    assert bubble_sort([2]) == [2]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    assert data is not sorted_data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [1, 2, 3, 4]
    sorted_data = bubble_sort(data)

    assert data == sorted_data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [3, 2, 1]
    manually_sorted_data = [1, 2, 3]
    sorted_data = bubble_sort(data)

    assert sorted_data == manually_sorted_data


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [1, 1, 1, 1]
    manually_sorted_data = [1, 1, 1, 1]
    sorted_data = bubble_sort(data)

    assert sorted_data == manually_sorted_data


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    data_1 = [1, 8, 9, 5, 2]
    manually_sorted_data_1 = [1, 2, 5, 8, 9]
    data_2 = [1.2, 1.1, 1.5]
    manually_sorted_data_2 = [1.1, 1.2, 1.5]
    data_3 = ["Daniil", "Olve", "Helge"]
    manually_sorted_data_3 = ["Daniil", "Helge", "Olve"]
    assert bubble_sort(data_1) == manually_sorted_data_1
    assert bubble_sort(data_2) == manually_sorted_data_2
    assert bubble_sort(data_3) == manually_sorted_data_3
