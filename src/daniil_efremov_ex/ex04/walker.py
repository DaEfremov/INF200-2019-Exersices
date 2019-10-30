# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov'
__email__ = 'daniil.vitalevich.efremov@nmbu.no'

import random


class Walker:
    def __init__(self, position, end_position):
        self.position = position
        self.end_position = end_position
        self.number_of_steps = 0

    def move(self):
        self.position += (-1) ** random.randint(0, 1)
        self.number_of_steps += 1

    def is_at_home(self):
        if self.position == self.end_position:
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

        while not walk.is_at_home():
            walk.move()

        path_len_list.append(walk.get_steps())

    return path_len_list


if __name__ == '__main__':

    distance_list = [1, 2, 5, 10, 20, 50, 100]
    number_of_simulations = 5

    for distance in distance_list:
        list_of_path_len = walk_home_simulation(distance,
                                                number_of_simulations)

        print(
            f"Distance:  {distance} -> Path lengths:"
            f"{sorted(list_of_path_len)}\n")
