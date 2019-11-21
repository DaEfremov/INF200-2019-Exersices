# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov', 'Sigurd Grøtan'
__email__ = 'daniil.vitalevich.efremov@nmbu.no', 'sgrotan@nmbu.no'

import chutes_simulation as cs


class TestBoard:
    """
    Tests for Board class.
    """

    def test_goal_reached(self):

        position_1 = 80
        position_2 = 100
        b = cs.Board(goal=90)
        assert b.goal_reached(position_1) is False
        assert b.goal_reached(position_2) is True

    def test_position_adjustment(self):

        position_1 = 1
        position_2 = 33
        position_3 = 20
        b = cs.Board(ladders=[(1, 40)], chutes=[(33, 3)])
        assert b.position_adjustment(position_1) == 40
        assert b.position_adjustment(position_2) == 3
        assert b.position_adjustment(position_3) == position_3


class TestPlayer:

    def test_move(self):

        p = cs.Player(cs.Board())
        pre_pos = p.position
        p.move()
        post_pos = p.position
        assert pre_pos != post_pos

    def test_move_less_than_1(self):

        for _ in range(10000):
            p = cs.Player(cs.Board())
            p.move()
            assert p.position > 0

    def test_move_not_chute_or_ladder(self):

        for _ in range(10000):
            p = cs.Player(cs.Board(ladders=[(1, 40)], chutes=[(33, 3)]))
            for _ in range(100):
                p.move()
                assert p.adjusted_position != 1 and p.adjusted_position != 33


class TestSimulation:

    def test_single_game(self):
        game = cs.Simulation()
        winner = game.single_game()

        if game.result_list[0][0] <= game.result_list[1][0]:
            assert winner[0] == game.result_list[0][0]

        else:
            assert winner[0] == game.result_list[1][0]

    def test_run_simulation(self):
        pass

    def test_get_results(self):
        pass

    def test_players_per_type(self):
        pass

    def test_winners_per_type(self):
        pass

    def test_durations_per_type(self):
        pass
