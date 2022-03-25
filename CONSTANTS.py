"""Algorithm CROSSOVER"""
CROSSOVER_PX_PROBABILITY = 0.7

"""Algorithm MUTATION"""
MUTATION_PM_PROBABILITY = 0.4

"""Algorithm SELECTION"""
SELECTION_TOURNAMENT_BATCH_SIZE = 5
SELECTION_TOURNAMENT_WINNERS_SIZE = 2

"""Algorithm ELITISM"""
ELITISM_IS_ON: bool = True
ELITISM_LIST_SIZE = 10

"""Genetic Algorithm"""
GA_POP_SIZE = 100
GA_ITERATIONS = 100

# 0 - roulette, 1 - tournament
GA_SELECTION = 1
SELECTION_NAME = {
    0: 'Roulette',
    1: 'Tournament'
}

"""Graph generator"""
GRAPH_SAVE: bool = False
GRAPH_STYLE = 'ggplot'
GRAPH_COLORS = {
    'best': 'g',
    'average': 'b',
    'worst': 'r'
}