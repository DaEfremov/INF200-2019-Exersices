# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov', 'Sigurd Grøtan'
__email__ = 'daniil.vitalevich.efremov@nmbu.no', 'sgrotan@nmbu.no'

from random import randint, shuffle


class Board:
    """Class that creates the board

    Parameters:
    ladders (list): List containing tuples from start to end position
    chutes (list): List containing tuples from start to end position
    goal (int): Integer that gives last tile on the board
    """
    default_ladders = [(1, 40), (8, 10), (36, 52), (43, 62),
                       (49, 79), (65, 82), (68, 85)]
    default_chutes = [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27),
                      (74, 12), (87, 70)]

    def __init__(self, ladders=None, chutes=None, goal=90):
        if ladders is None:
            ladders = Board.default_ladders
        if chutes is None:
            chutes = Board.default_chutes
        self.ladders = ladders
        self.chutes = chutes
        self.goal = goal

    def goal_reached(self, position):
        """Class method checks if player has reached the goal position

        Parameters:
        position (int): Integer of players position

        Returns:
        bool: Returning true or false if goal is reached or not"""
        if position >= self.goal:
            return True
        else:
            return False

    def position_adjustment(self, position):
        """Class method checks if the position the player
        reached has a chute or a ladder on it

        Parameters:
        position (int): Integer of players position

        Returns:
        int: The adjusted position"""
        for ladder in self.ladders:
            if position == ladder[0]:
                position = ladder[1]

        for chute in self.chutes:
            if position == chute[0]:
                position = chute[1]

        return position


class Player:
    """Class that creates the player

    Parameters:
    board (class): Takes the class board created as par."""

    def __init__(self, board):
        self.board = board
        self.position = 0
        self.adjusted_position = 0

    def move(self):
        """Class method makes the player do a move,
        and adjustes to the correct end-position

        Parameters:
        None

        Returns:
        None
        """
        self.position = self.adjusted_position
        self.position += randint(1, 6)
        self.adjusted_position = self.board.position_adjustment(self.position)


class ResilientPlayer(Player):
    """Subclass of the Player class with different
    set of rules for when player hits a chute

    Parameters:
    board (class): Takes the class board as par.
    extra-steps (int): Makes extra steps forward after sliding down a chute
    """

    def __init__(self, board, extra_steps=1):
        self.extra_steps = extra_steps
        super().__init__(board)

    def move(self):
        """Class method makes the player move extra steps
        forward after sliding down a chute

        Parameters:
        None

        Returns:
        None
        """
        super().move()
        if self.position > self.adjusted_position:
            self.adjusted_position += self.extra_steps


class LazyPlayer(Player):
    """Subclass of the Player class with different
    set of rules for when a players hits a ladder

    Parameters:
    board (class): Takes the class board as par.
    dropped-steps (int): Makes extra steps backwards after climbing a ladder
    """

    def __init__(self, board, dropped_steps=1):
        self.dropped_steps = dropped_steps
        super().__init__(board)

    def move(self):
        """Class method makes the player move back dropped-steps after
        climbing up a ladder

        Parameters:
        None

        Returns:
        None """
        super().move()
        if self.position < self.adjusted_position:
            if (self.adjusted_position - self.dropped_steps) <= self.position:
                self.adjusted_position = self.position
            else:
                self.adjusted_position -= self.dropped_steps


class Simulation:
    """Class that simulates a number of games of Chutes and Ladders

    Parameters:
    player_field (list): list of classes
    board (class): Takes the class board as par.
    seed (int): Takes a integer and uses to make a seed
    randomize_players (bool): Chooses whether or not to shuffle player_field
    """

    def __init__(self, player_field=[Player, Player], board=Board(), seed=123,
                 randomize_players=True):

        self.player_field = player_field
        self.board = board
        self.seed = seed
        self.result_list = []
        self.winner_list = []
        if randomize_players:
            shuffle(self.player_field)

    def single_game(self):
        """Class method performs a single game of chutes and ladders

        Parameters:
        None

        Returns:
        tuple: Tuple with number of steps,
        and name of the winner of single game
        """
        for player_class in self.player_field:
            number_of_steps = 0
            player = player_class(self.board)
            while not self.board.goal_reached(player.adjusted_position):
                player.move()
                number_of_steps += 1

            self.result_list.append((number_of_steps, player_class.__name__))

        winner = self.result_list[0]
        for result in self.result_list[1:]:
            if result[0] < winner[0]:
                winner = result

        return winner

    def run_simulation(self, num_sim):
        """Class method performs a given number(num_sim)
         of simulations of a single game

        Parameters:
        num_sim (int): Number of simulations for
        a single game of chutes and ladders

        Returns:
        None   """
        for _ in range(num_sim):
            self.winner_list.append(self.single_game())

    def get_results(self):
        """Class method returns winner_list found from run_simulation

        Parameters:
        None

        Returns:
        list: Returns the list of winners.
        """
        return self.winner_list

    def durations_per_type(self):
        """Class method that counts number of steps each player does
        in every game of chutes and ladders.

        Parameters:
        None

        Returns:
        dict: Dictionary with player-name as key and list of moves as value.

        """
        durations_dict = {'Player': [], 'LazyPlayer': [],
                          'ResilientPlayer': []}

        for player in self.result_list:
            durations_dict[player[1]].append(player[0])

        return durations_dict

    def winners_per_type(self):
        """
        Class method that counts number of times
        a type of player has won the game.

        Parameters:
        None

        Returns:
        dict: Dictionary with player-name as key
        and a integer of number of wins as value 
        """
        winner_dict = {'Player': 0, 'LazyPlayer': 0, 'ResilientPlayer': 0}

        for winner in self.winner_list:
            winner_dict[winner[1]] += 1

        return winner_dict

    def players_per_type(self):
        """
        Class method which counts number of players per player type.

        Parameters:
        None

        Returns:
        dict: Dictionary containing player names as keys and
        corresponding player count as value.
        """
        players_dict = {'Player': 0, 'LazyPlayer': 0, 'ResilientPlayer': 0}

        for player in self.player_field:
            players_dict[player.__name__] += 1

        return players_dict
