from individual import *
import random
import CONSTANTS



class TournamentSelection:
    tournament_batch_size = CONSTANTS.SELECTION_TOURNAMENT_BATCH_SIZE
    tournament_winners_size = CONSTANTS.SELECTION_TOURNAMENT_WINNERS_SIZE

    @classmethod
    def select(cls, population: 'list[Individual]'):
        new = []

        for _ in range(2):
            competitors = random.choices(population, k=cls.tournament_batch_size)
            new.append(cls.__select_winner(competitors))

        return new[0], new[1]

    @classmethod
    def __select_winner(cls, competitors: 'list[Individual]'):
        winner = competitors[0]

        for elem in competitors:
            if elem.fitness > winner.fitness:
                winner = elem

        return winner


class RouletteSelection:

    """Select Individuals by Roulette selection"""
    @classmethod
    def select(cls, population: 'list[Individual]'):
        new = []

        accumulated_pobabilites = cls.create_accumulated_pobabilites(population)

        for _ in range(2):
            new.append(Individual.copy(cls.single_roulette_wheel(population, accumulated_pobabilites)))

        return new[0], new[1]

    '''Random individual choose'''
    @classmethod
    def single_roulette_wheel(cls, population: 'list[Individual]', accumulated_probabilities: 'list[float]') -> Individual:
        random_selection = random.random()

        # Select first matching element
        for elem, probability in zip(population, accumulated_probabilities):
            if probability >= random_selection:
                return elem

    '''Calculate probabilities for all population - 
       calculating how much space they have taken from the interval <0, 1> '''
    @classmethod
    def create_accumulated_pobabilites(cls, population: 'list[Individual]') -> 'list[float]':
        accumulated_pobabilites = []
        probability_sum = 0
        fitness_sum = cls.calculate_fitness_sum(population)

        for elem in population:
            probability_sum += elem.fitness / fitness_sum
            accumulated_pobabilites.append(probability_sum)

        # Our interval is <0, 1> so last element should have value = 1
        if accumulated_pobabilites:
            accumulated_pobabilites[-1] = 1

        return accumulated_pobabilites

    @classmethod
    def calculate_fitness_sum(cls, population: 'list[Individual]') -> int:
        return sum(list(map(lambda x: x.fitness, population)))
