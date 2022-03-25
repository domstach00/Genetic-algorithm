from individual import *
import random
import CONSTANTS


class Elitism:
    elite_count: int = CONSTANTS.ELITISM_LIST_SIZE
    elites: 'list[Individual]' = []

    '''Select elites in population and copy them into static list'''
    def get_elite_copies(self, population: 'list[Individual]'):
        if self.elite_count > 0:
            population = sorted(population)
            elites = population[:int(self.elite_count)]
            self.elites = [Individual.copy(elem) for elem in elites]
        # print(f"\tCURRENT ELITE: {elites[0].list}, score: {elites[0].score}")

    '''Replace the weakest individuals with elites'''
    def append_elites(self, population: 'list[Individual]'):
        if self.elite_count > 0:
            population = sorted(population)
            population = population[0:-self.elite_count] + self.elites
