from genetic_algorithm import *
from make_graph.observation import *


def run_easy():
    print("\n\n\tLEVEL: easy")
    config = Config(3, 3, 9)
    config.load_data('easy')
    ga = GeneticAlgorithm(config)
    ga.initialise()
    ga.run()


def run_flat():
    print("\n\n\tLEVEL: flat")
    config = Config(1, 12, 12)
    config.load_data('flat')
    ga = GeneticAlgorithm(config)
    ga.initialise()
    ga.run()


def run_hard():
    print("\n\n\tLEVEL: hard")
    config = Config(5, 6, 24)
    config.load_data('hard')
    ga = GeneticAlgorithm(config)
    ga.initialise()
    ga.run()


if __name__ == '__main__':
    run_easy()
    run_flat()
    run_hard()
