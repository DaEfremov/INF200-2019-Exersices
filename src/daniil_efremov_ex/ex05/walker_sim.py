# -*- coding: utf-8 -*-

__author__ = 'Daniil Efremov'
__email__ = 'daniil.vitalevich.efremov@nmbu.no'

import random


class Simulation:
    def __init__(self, start, home, seed):
        self.start = start
        self.home = home
        self.seed = random.seed(seed)

    def single_walk(self):
        start = self.start
        home = self.home
        number_of_steps = 0
        while start is not home:
            start += (-1) ** random.randint(0, 1)
            number_of_steps += 1

        return number_of_steps

    def run_simulation(self, num_walks):

        self.num_walks = num_walks
        self.list_of_num = []

        for index in range(num_walks):
            self.list_of_num.append(self.single_walk())

        return self.list_of_num


if __name__ == '__main__':
    pos_1 = 0
    pos_2 = 10
    seed_1 = 12345
    seed_2 = 54321
    num_of_simulations = 20

    simulation_1 = Simulation(pos_1, pos_2, seed_1)
    case_1_1 = sorted(simulation_1.run_simulation(num_of_simulations))
    case_1_2 = sorted(simulation_1.run_simulation(num_of_simulations))
    simulation_2 = Simulation(pos_2, pos_1, seed_1)
    case_2_1 = sorted(simulation_2.run_simulation(num_of_simulations))
    case_2_2 = sorted(simulation_2.run_simulation(num_of_simulations))
    simulation_3 = Simulation(pos_1, pos_2, seed_2)
    case_3_1 = sorted(simulation_3.run_simulation(num_of_simulations))
    simulation_4 = Simulation(pos_2, pos_1, seed_2)
    case_4_1 = sorted(simulation_4.run_simulation(num_of_simulations))

    print(f"""Case 1 - Run 1:\nStart-position: {pos_1}, End-position: {pos_2},
Seed: {seed_1}, List: {case_1_1} \n
Case 1 - Run 2:\nStart-position: {pos_1}, End-position: {pos_2}, 
Seed: {seed_1}, List: {case_1_2}\n
Case 2: - Run 1:\nStart-position: {pos_2}, End-position: {pos_1}, 
Seed: {seed_1}, List: {case_2_1}\n
Case 2: - Run 2:\nStart-position: {pos_2}, End-position: {pos_1}, 
Seed: {seed_1}, List: {case_2_2}\n
Case 3:\nStart-position: {pos_1}, End-position: {pos_2}, 
Seed: {seed_2}, List: {case_3_1}\n
Case 4:\nStart-position: {pos_2}, End-position: {pos_1}, 
Seed: {seed_2}, List: {case_4_1}\n
    """)
