import math
import random
from config import *


class Individual:
    def __init__(self, config: Config):
        self.config: Config = config
        self.list: list[int] = list(range(self.config.machine_count))
        self.score: int = None
        self.fitness: float = None

    '''Random method'''
    def shuffle(self, elements=None):
        if elements is None:
            elements = self.list
        random.shuffle(elements)
        # We choose exactly as many random items as there are machines to be deployed
        self.list = elements[0:self.config.machine_count]

    '''Calculate score'''
    def calc_score(self):
        score = 0
        connections = self.config.connections

        for src in connections:
            for dest in connections[src]:
                cost = self.config.costs[(src, dest)]
                flow = self.config.flows[(src, dest)]
                source_position = self.list[src]
                dest_position = self.list[dest]
                score += cost * flow * self.calc_manhattan(source_position, dest_position)
        self.score = score
        self.fitness = self.__calc_fitness()

    def __calc_fitness(self):
        return math.e**(1 / self.score)

    '''Calculate Manhattan distance'''
    def calc_manhattan(self, source: int, dest: int):
        x = abs(source % self.config.height - dest % self.config.height)
        y = abs(source // self.config.height - dest // self.config.height)
        return x + y

    @classmethod
    def copy(cls, other):
        new: Individual = cls(other.config)
        new.list = list(other.list)     # We need to add a list constructor so that no reference is passed
        new.score = other.score
        new.fitness = other.fitness
        return new

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score
