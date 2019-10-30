# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov'
__email__ = 'daniil.vitalevich.efremov@nmbu.no'


class LCGRand:
    a = 16807
    m = 2 ** 31 - 1

    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        self.seed = LCGRand.a * self.seed % LCGRand.m

        return self.seed


class ListRand:
    def __init__(self, nummer_liste):
        self.nummer_liste = nummer_liste
        self.index = 0

    def rand(self):

        if self.index >= len(self.nummer_liste):
            raise RuntimeError

        else:

            next_number = self.nummer_liste[self.index]
            self.index += 1

            return next_number


if __name__ == '__main__':
    seed_1 = 1
    lcg_test = LCGRand(seed_1)

    print(f"LCGRand tester:\nWith a seed of {seed_1}\nRun 1: "
          f"{lcg_test.rand()}\nRun 2: "
          f"{lcg_test.rand()}\nRun 3: "
          f"{lcg_test.rand()}\n ")

    test_liste = [1, 2, 3, 4, 5]
    listrand_test = ListRand(test_liste)

    print(f"ListRand tester:\nWith a list of {test_liste}\nRun 1: "
          f"{listrand_test.rand()}\nRun 2: "
          f"{listrand_test.rand()}\nRun 3: "
          f"{listrand_test.rand()} ")
