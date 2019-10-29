# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov', 'Sigurd Grøtan'
__email__ = 'daniil.vitalevich.efremov@nmbu.no', 'sgrotan@nmbu.no'

import random as rd
import statistics


def throw_dice():
    return rd.randint(1, 6)


def check_ladder_or_snake(position):
    critical_pos = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79,
                    65: 82, 68: 85, 24: 5, 33: 3, 42: 30,
                    56: 37, 64: 27, 74: 12, 87: 70}

    if position in critical_pos:
        position = critical_pos[position]

    return position


def create_players(num_players):
    players = []

    for i in range(num_players):
        players.append(0)

    return players


def make_a_move(players):
    for index, old_pos in enumerate(players):

        dice = throw_dice()
        new_pos = old_pos + dice

        if new_pos > 90:
            new_pos = 90 - (dice - (90 - old_pos))

        new_pos = check_ladder_or_snake(new_pos)

        players[index] = new_pos

    return players


def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """

    players_positions = create_players(num_players)
    num_of_moves = 0

    while max(players_positions) < 90:

        num_of_moves += 1
        players_positions = make_a_move(players_positions)

    return num_of_moves


def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """

    num_moves = []

    for i in range(num_games):
        num_moves.append(single_game(num_players))

    return num_moves


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """
    rd.seed(seed)
    num_moves = multiple_games(num_games, num_players)
    return num_moves


if __name__ == '__main__':

    experiment_list = multi_game_experiment(100, 4, 1)
    sorted_experiment_list = sorted(experiment_list)
    median = (sorted_experiment_list[49] + sorted_experiment_list[50]) / 2
    mean = sum(sorted_experiment_list) / len(sorted_experiment_list)
    stdev = statistics.stdev(sorted_experiment_list)

    print(f"""Shortest game: {min(sorted_experiment_list)} 
    \nLongest game: {max(sorted_experiment_list)} 
    \nMedian: {median}
    \nMean: {mean}
    \nStandard Deviation: {stdev}
    """)
