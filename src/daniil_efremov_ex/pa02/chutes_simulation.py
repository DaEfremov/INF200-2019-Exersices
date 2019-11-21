# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov', 'Sigurd Grøtan'
__email__ = 'daniil.vitalevich.efremov@nmbu.no', 'sgrotan@nmbu.no'

from random import randint, shuffle
#default_ladders = [(1,40), (8,10), (36,52), (43,62),
 #                               (49,79), (65,82), (68,85)]
  #  default_chutes = [(24,5), (33,3), (42,30), (56,37), (64,27),
  #                              (74,12), (87,70)]

class Board:
    def __init__(self, ladders=[(1,40), (8,10), (36,52), (43,62),
                                (49,79), (65,82), (68,85)],
                        chutes=[(24,5), (33,3), (42,30), (56,37), (64,27),
                                (74,12), (87,70)], goal=90):
        self.ladders = ladders
        self.chutes = chutes
        self.goal = goal

    def goal_reached(self, position):
        if position >= self.goal:
            return True


    def position_adjustment(self, position):
        for ladder in self.ladders:
            if position == ladder[0]:
                position = ladder[1]

        for chute in self.chutes:
            if position == chute[0]:
                position = chute[1]

        return position


class Player:

    def __init__(self, board):
        self.board = board
        self.position = 0
        self.adjusted_position = 0


    def move(self):
        self.position = self.adjusted_position
        self.position += randint(1, 6)
        self.adjusted_position = self.board.position_adjustment(self.position)


class ResilientPlayer(Player):

    def __init__(self, board, extra_steps=1):
        self.extra_steps = extra_steps
        super().__init__(board)

    def move(self):
        super().move()
        if self.position > self.adjusted_position:
            self.adjusted_position += self.extra_steps


class LazyPlayer(Player):

    def __init__(self, board, dropped_steps=1):
        self.dropped_steps = dropped_steps
        super().__init__(board)

    def move(self):
        super().move()
        if self.position < self.adjusted_position:
            if (self.adjusted_position - self.dropped_steps) <= self.position:
                self.adjusted_position = self.position
            else:
                self.adjusted_position -= self.dropped_steps



class Simulation:

    def __init__(self, player_field=[Player, Player], board=Board(), seed=123, randomize_players=True):
        self.player_field = player_field
        self.board = board
        self.seed = seed
        self.result_list = []
        if randomize_players:
            shuffle(self.player_field)

    def single_game(self):
        game_results = []
        for player_class in self.player_field:
            number_of_steps = 0
            player = player_class(self.board)
            while not self.board.goal_reached(player.adjusted_position):
                player.move()
                number_of_steps += 1

            game_results.append((number_of_steps, player_class.__name__))

        winner = game_results[0]
        for result in game_results[1:]:
            if result[0] < winner[0]:
                winner = result

        return winner


    def run_simulation(self, num_sim):
        for _ in range(num_sim):
            self.result_list.append(self.single_game())

    def get_results(self):
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

sim = Simulation([Player, Player, ResilientPlayer, ResilientPlayer,ResilientPlayer, LazyPlayer])

sim.run_simulation(5)
print(sim.get_results())