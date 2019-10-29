# -*- coding: utf-8 -*-

"""
Acceptance test suite for EX04.
Your code should pass these tests before submission.
"""

import pytest
import random
# from myrand import LCGRand, ListRand
# from walker import Walker
# I did not manage to make the imports work, so i copied in my code:

__author__ = 'Hans Ekkehard Plesser'
__email__ = 'hans.ekkehard.plesser@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        a = 16807
        m = 2 ** 31 - 1
        self.seed = a * self.seed % m

        return self.seed


class ListRand:
    def __init__(self, nummer_liste):
        self.nummer_liste = nummer_liste
        self.nr_i_lista = 0

    def rand(self):

        if self.nr_i_lista >= len(self.nummer_liste):
            raise RuntimeError

        else:

            neste_nummer = self.nummer_liste[self.nr_i_lista]
            self.nr_i_lista += 1

            return neste_nummer


class Walker:
    def __init__(self, position, end_position):
        self.position = position
        self.end_position = end_position
        self.number_of_steps = 0

    def move(self):
        self.position += (-1) ** random.randint(0, 1)
        self.number_of_steps += 1

    def is_at_home(self):
        if self.position >= self.end_position:
            return True
        else:
            return False

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.number_of_steps


def walk_home_simulation(distance, number_of_simulations):
    path_len_list = []
    for index in range(number_of_simulations):

        walk = Walker(0, distance)

        while walk.is_at_home() is False:
            walk.move()

        path_len_list.append(walk.get_steps())

    return path_len_list


def test_lcg():
    """Test that LCG generator works."""

    lcg = LCGRand(346)
    assert lcg.rand() == 5815222
    assert lcg.rand() == 1099672039


def test_list_rng():
    """Test that ListRNG generator works."""
    numbers = [4, 5, 29, 11]
    lr = ListRand(numbers)
    assert [lr.rand() for _ in range(len(numbers))] == numbers
    with pytest.raises(RuntimeError):
        lr.rand()


def test_walker():
    """Test that Walker class can be used as required."""

    start, home = 10, 20
    w = Walker(start, home)
    assert not w.is_at_home()
    w.move()
    assert w.get_position() != start
    w.move()
    assert w.get_steps() == 2
