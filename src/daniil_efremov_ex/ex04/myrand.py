# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov'
__email__ = 'daniil.vitalevich.efremov@nmbu.no'


class LSGRand:
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
