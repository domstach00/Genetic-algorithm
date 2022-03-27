from individual import *
import random
import CONSTANTS


class Mutation:
    Pm_probability = CONSTANTS.MUTATION_PM_PROBABILITY

    '''Change single gens and calculate new score'''
    @classmethod
    def change_individual(cls, individual: Individual):
        for elem_number in range(len(individual.list)):
            if random.random() <= cls.Pm_probability:
                new = random.randint(0, individual.config.machine_count - 1)
                try:
                    individual.list[individual.list.index(new)] = individual.list[elem_number]
                    individual.list[elem_number] = new
                except ValueError:
                    print(f"Value Error: new {new}, elem_number: {elem_number}")
                    individual.list[elem_number] = new

        individual.calc_score()
