from lab1_Dominik_Stachowiak import *
import random
import CONSTANTS


class Mutation:
    Pm_probability = CONSTANTS.MUTATION_PM_PROBABILITY

    def __init__(self, individual: Individual):
        self.individual = individual

    '''Change single gens and calculate new score'''
    def change_individual(self):
        for elem_number in range(len(self.individual.list)):
            if random.random() <= self.Pm_probability:
                new = random.randint(0, self.individual.config.machine_count)
                try:
                    self.individual.list[self.individual.list.index(new)] = self.individual.list[elem_number]
                    self.individual.list[elem_number] = new
                except ValueError:
                    self.individual.list[elem_number] = new

        self.individual.calc_score()
