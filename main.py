from lab1_Dominik_Stachowiak import *
from algorithms.crossover import *
from algorithms.mutation import *

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
    for i in range(9):
        elem = Individual(config)
        elem.shuffle(elem.list)
        elem.calc_score()
        list.append(elem)

    list[0].list = [0, 3, 2, 1]
    list[0].config.machine_count = 3
    list[1].list = [3, 4, 1, 7]

    m = Mutation(list[0])
    m.change_individual()
    print(m.individual.list)

    # c = Crossover(list[0], list[1])
    # c.cross_parents()
    print()




if __name__ == '__main__':
    do()
