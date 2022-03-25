from individual import *
from algorithms.crossover import *
from algorithms.mutation import *
from algorithms.selection import *
from genetic_algorithm import *


def lab1():
    # Ustawienie konfuguracji wstępnej
    config_easy = Config(3, 3, 9)
    config_flat = Config(1, 12, 12)
    config_hard = Config(5, 6, 24)
    config_easy.load_data('easy')

    adaptation_f = Individual(config_easy)
    print("Pierwotny wygląd listy:", adaptation_f.list)
    adaptation_f.shuffle(adaptation_f.list)  # tasujemy liste
    print("Lista po przetasowaniu:", adaptation_f.list)
    adaptation_f.calc_score()
    print("Wynik funkcji przystosowania:", adaptation_f.score)


def do():
    list = []
    config = Config(3, 3, 9)
    config.load_data('easy')
    invidual = Individual(config)
    invidual.list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    Mutation.change_individual(invidual)
    print(invidual.list)


def run():
    config = Config(3, 3, 9)
    config.load_data('easy')
    ga = GeneticAlgorithm(config)
    ga.initialise()
    ga.run()


def run_flat():
    config = Config(5, 6, 24)
    config.load_data('hard')
    ga = GeneticAlgorithm(config)
    ga.initialise()
    ga.run()


if __name__ == '__main__':
    run()
    # list1 = [0, 1, 2, 3, 4, 5, 6, 7]
    # list2 = ['X', 'Y', 'Z']
    # list1[-1] = 'H'
    # print(list1)
