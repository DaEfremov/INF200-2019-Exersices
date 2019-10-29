# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov'
__email__ = 'daniil.vitalevich.efremov@nmbu.no'


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


if __name__ == '__main__':
    seed_1 = 1
    LCG_test_1 = LCGRand(seed_1)

    print(f"LCGRand tester:\nWith a seed of {seed_1}\nRun 1: "
          f"{LCG_test_1.rand()}\nRun 2: "
          f"{LCG_test_1.rand()}\nRun 3: "
          f"{LCG_test_1.rand()}\n ")

    test_liste = [1, 2, 3, 4, 5]
    ListRand_test_1 = ListRand(test_liste)

    print(f"ListRand tester:\nWith a list of {test_liste}\nRun 1: "
          f"{ListRand_test_1.rand()}\nRun 2: "
          f"{ListRand_test_1.rand()}\nRun 3: "
          f"{ListRand_test_1.rand()} ")
