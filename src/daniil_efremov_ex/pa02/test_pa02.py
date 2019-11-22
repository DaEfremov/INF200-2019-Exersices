# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov', 'Sigurd Grøtan'
__email__ = 'daniil.vitalevich.efremov@nmbu.no', 'sgrotan@nmbu.no'

import chutes_simulation as cs
import pytest


class TestBoard:
    """
    Tests for Board class.
    """

    def test_goal_reached(self):
        """Test that checks whether 2 positions have reached goal or not"""

        position_1 = 80
        position_2 = 100
        b = cs.Board(goal=90)
        assert b.goal_reached(position_1) is False
        assert b.goal_reached(position_2) is True

    def test_position_adjustment(self):
        """Test that checks if the position is changed when
        player lands on the chute or ladder tile."""

        position_1 = 1
        position_2 = 33
        position_3 = 20
        b = cs.Board(ladders=[(1, 40)], chutes=[(33, 3)])
        assert b.position_adjustment(position_1) == 40
        assert b.position_adjustment(position_2) == 3
        assert b.position_adjustment(position_3) == position_3


class TestPlayer:
    """Test for Player class"""

    def test_move(self):
        """Test that checks if position is changed when
        the class method move() is being used"""

        p = cs.Player(cs.Board())
        pre_pos = p.position
        p.move()
        post_pos = p.position
        assert pre_pos != post_pos

    def test_move_less_than_1(self):
        """Test that checks if a player can get to a negative numbered tile"""

        for _ in range(10000):
            p = cs.Player(cs.Board())
            p.move()
            assert p.position > 0

    def test_move_not_chute_or_ladder(self):
        """Test that checks if a player that hits a chute or ladder tile
        will move along to the assigned tile right away"""
        for _ in range(10000):
            p = cs.Player(cs.Board(ladders=[(1, 40)], chutes=[(33, 3)]))
            for _ in range(100):
                p.move()
                assert p.adjusted_position != 1 and p.adjusted_position != 33


class TestSimulation:
    """Tests for simulation class"""

    def test_single_game(self):
        """Test that checks whether the right winner is chosen properly"""
        game = cs.Simulation()
        winner = game.single_game()

        if game.result_list[0][0] <= game.result_list[1][0]:
            assert winner[0] == game.result_list[0][0]

        else:
            assert winner[0] == game.result_list[1][0]

    def test_run_simulation(self):
        """Test that checks if the length of the winner_list is
        the same as the num_sim(int) input."""
        game = cs.Simulation()
        num_sim = 5
        game.run_simulation(num_sim)

        assert len(game.winner_list) == num_sim

    def test_get_results(self):
        """Test that checks if winner_list is a list, and if the elements
        in the lists are tuples."""
        game = cs.Simulation()
        game.run_simulation(1)
        type_1 = game.winner_list
        type_2 = game.winner_list[0]

        assert isinstance(type_1, list)
        assert isinstance(type_2, tuple)

    def test_players_per_type(self):
        """Test that checks if the value in
        the given dictionary is an integer"""
        game = cs.Simulation()
        game.run_simulation(1)
        player_dict = game.players_per_type()

        assert isinstance(player_dict.get('Player'), int)

    def test_winners_per_type(self):
        """Test that checks if the value in
        the given dictionary is an integer"""
        game = cs.Simulation()
        game.run_simulation(1)
        winner_dict = game.winners_per_type()

        assert isinstance(winner_dict.get('Player'), int)

    def test_durations_per_type(self):
        """Test that checks if the value in
        the given dictionary is a list"""
        game = cs.Simulation()
        game.run_simulation(1)
        duration_dict = game.durations_per_type()

        assert isinstance(duration_dict.get('Player'), list)
