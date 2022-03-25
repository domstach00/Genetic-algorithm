import random
import time

from config import *


class Individual:
    def __init__(self, config: Config):
        self.config: Config = config
        self.list: list[int] = list(range(self.config.width * self.config.height))
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
        print(connections)
        for key in connections:
            for value in connections[key]:
                cost = self.config.costs[(key, value)]
                flow = self.config.flows[(key, value)]
                source_position = self.list.index(key)
                dest_position = self.list.index(value)
                score += cost * flow * \
                         (abs(source_position % self.config.width - dest_position % self.config.width) +
                          abs(source_position // self.config.width - dest_position // self.config.width))
        self.score = score
        self.fitness = 1 / score

    # def calc_score(self):
    #     score = 0
    #     connections = self.config.connections
    #     for source in connections:
    #         for dest in connections[source]:
    #             # Read cost i flow for each connection
    #             # cost = self.config.costs[(source, dest)]
    #             # flow = self.config.flows[(source, dest)]
    #             score += self.calculate_score_helper(source, dest)
    #
    #             # Calculate objective function
    #             # score += cost * flow * self.calc_manhattan(self.list[source], self.list[dest])
    #     self.score = score
    #     self.fitness = 1 / score

    def calculate_score_helper(self, source, dest):
        distance = self.calculate_distance(source, dest)
        cost = self.config.costs[(source, dest)]
        flow = self.config.flows[(source, dest)]
        print(f"cost: {cost}, flow: {flow}")
        return distance * cost * flow

    def calculate_distance(self, source, dest):
        print("\n\n")
        source_position = self.list[source]
        print(f"source: {source_position}")
        dest_position = self.list[dest]
        print(f"dest: {dest_position}")
        width = self.config.width
        print(f"width: {width}")
        height = self.config.height
        print(f"height: {height}")
        res = abs(source_position % width - dest_position % width) + \
               abs(source_position // height - dest // height)
        print(f"RES: {dest_position % width}")
        return res

    '''Calculate Manhattan distance'''
    def calc_manhattan(self, source: int, dest: int) -> int:
        x = abs(source % self.config.width - dest % self.config.width)
        y = abs(source // self.config.height - dest // self.config.height)
        return x + y

    @classmethod
    def copy(cls, other):
        new: Individual = cls(other.config)
        new.list = other.list
        new.score = other.score
        new.fitness = other.fitness
        return new

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score
