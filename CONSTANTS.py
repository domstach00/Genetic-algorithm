"""Algorithm CROSSOVER"""
CROSSOVER_PX_PROBABILITY = 0.7

"""Algorithm MUTATION"""
MUTATION_PM_PROBABILITY = 0.1

"""Genetic Algorithm"""
GA_POP_SIZE = 1000
GA_ITERATIONS = 100

# 0 - Child replace parent, 1 - Child replace the worst individual
GA_CHILD_REPLACE_WORST = 1
CHILD_REPLACE = {
    0: False,
    1: True
}

"""Algorithm SELECTION"""
SELECTION_TOURNAMENT_BATCH_SIZE = 500

"""Algorithm ELITISM"""
ELITISM_IS_ON: bool = False
ELITISM_LIST_SIZE = int(GA_POP_SIZE * 0.02)     # 2%

# 0 - roulette, 1 - tournament
GA_SELECTION = 0
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

"""CONSOLE"""
CONSOLE_PRINT_ITERATIONS: bool = True
CONSOLE_PRINT_LAST_ITERATION: bool = True
CONSOLE_PRINT_BEST_SETUP: bool = False
