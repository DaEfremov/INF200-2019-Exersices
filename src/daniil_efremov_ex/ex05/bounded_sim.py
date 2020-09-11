# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov'
__email__ = 'daniil.vitalevich.efremov@nmbu.no'

import random


class Walker:
    def __init__(self, start, home):
        self.start = start
        self.home = home
        self.number_of_steps = 0

    def move(self):
        self.start += (-1) ** random.randint(0, 1)
        self.number_of_steps += 1

    def is_at_home(self):
        if self.start >= self.home:
            return True
        else:
            return False

    def get_position(self):
        return self.start

    def get_steps(self):
        return self.number_of_steps


class Simulation:
    def __init__(self, start, home, seed):
        self.start = start
        self.home = home
        self.seed = seed

    def single_walk(self):
        walk = Walker(self.start, self.home)

        while self.start is not self.home:
            walk.move()

        return walk.get_position()

    def run_simulation(self, num_walks):
        random.seed(self.seed)
        self.num_walks = num_walks
        self.list_of_num = []

        for index in range(num_walks):
            self.list_of_num.append(self.single_walk())

        return self.list_of_num


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        self.left_lim = left_limit
        self.right_lim = right_limit
        super().__init__(start, home)

    def make_bounded_move(self):

        if self.start >= self.left_lim and self.start <= self.right_lim:
            Walker.move(self)
            if self.start < self.left_lim:
                self.start = self.left_lim
            if self.start > self.right_lim:
                self.start = self.right_lim


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        self.left_limit = left_limit
        self.right_limit = right_limit
        super().__init__(start, home, seed)

    def bounded_walk(self):
        walk = BoundedWalker(self.start, self.home,
                             self.left_limit, self.right_limit)
        while not walk.is_at_home():
            walk.make_bounded_move()

        return walk.get_steps()

    def bounded_simulation(self, num_walks):
        random.seed(self.seed)
        results = []

        for index in range(num_walks):
            results.append(self.bounded_walk())

        return results


if __name__ == '__main__':
    num_walks = 20
    home = 20
    start = 0
    seed = 1
    right_limit = 20
    left_limit = [0, -10, -100, -1000]

    for value in left_limit:
        simulation = BoundedSimulation(start, home, seed, value, right_limit)
        case = simulation.bounded_simulation(num_walks)

        print(f"Left boundary: {value}\nCurrent list: {sorted(case)}\n")
