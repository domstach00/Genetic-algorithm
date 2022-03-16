from data import Config
from individual import Individual

config = Config(3, 3, 9, 'data/easy_cost.json', 'data/easy_flow.json')

individual = Individual(config)

individual.shuffle()

print(individual.array)

individual.calculate_score()

print(individual.score)