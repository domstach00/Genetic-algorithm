from individual import *
from math import *


class Observation:

    def __init__(self, list_of_individuals: 'list[Individual]'):
        self.list_of_individuals: 'list[Individual]' = list_of_individuals
        self.best_value: int = self.__find_best_value()
        self.worst_value: int = self.__find_worst_value()
        self.avg_value = self.__find_avg_value()

    def print_resoults(self):
        print(f"Best: {self.best_value}, Worst: {self.worst_value}, Avg: {self.avg_value}")

    def __find_avg_value(self):
        return sum(elem.score for elem in self.list_of_individuals) / len(self.list_of_individuals)

    def __find_best_value(self):
        best: int = self.list_of_individuals[0].score
        for elem in self.list_of_individuals:
            if best > elem.score:
                best = elem.score
        return best

    def __find_worst_value(self):
        worst: int = self.list_of_individuals[0].score
        for elem in self.list_of_individuals:
            if worst < elem.score:
                worst = elem.score
        return worst
