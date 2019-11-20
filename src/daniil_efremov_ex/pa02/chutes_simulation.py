# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov', 'Sigurd Grøtan'
__email__ = 'daniil.vitalevich.efremov@nmbu.no', 'sgrotan@nmbu.no'

from random import randint


class Board:

    def __init__(self, ladders=[(1, 4), (5, 16)], chutes=[(9, 2), (12, 3)], goal=90):
        self.ladders = ladders
        self.chutes = chutes
        self.goal = goal

    def goal_reached(self, player):
        return False

    def position_adjustment(self, pos):
        return pos + randint(1, 6)


class Player:

    def __init__(self, board):
        self.board = board

    def move(self):
        pass


class ResilientPlayer(Player):

    def __init__(self, board, extra_steps=4):
        self.extra_steps = extra_steps
        super().__init__(board)


class LazyPlayer(Player):

    def __init__(self, board, dropped_steps=3):
        self.dropped_steps = dropped_steps
        super().__init__(board)


class Simulation:

    def __init__(self, player_field=[Player, Player], board=Board(), seed=123, randomize_players=True):
        self.player_field = player_field
        self.board = board
        self.seed = seed
        self.randomize_players = randomize_players
        self.result_list = []

    def single_game(self):
        return 1, 'Player'

    def run_simulation(self, num_sim):
        for _ in range(num_sim):
            self.result_list.append((1, 'Player'))

    def get_results(self, a_number=2):
        return self.result_list

    def players_per_type(self):
        player_dict = {'Player': 0, 'LazyPlayer': 0, 'ResilientPlayer': 0}
        #        for player in self.player_field:
        #            player_name = player.__name__
        #            player_dict[player_name] += 1
        return player_dict

    def winners_per_type(self):
        return {'Player': 0, 'LazyPlayer': 0, 'ResilientPlayer': 0}

    def durations_per_type(self):
        return {'Player': [0, 0], 'LazyPlayer': [0, 0], 'ResilientPlayer': [0, 0]}
