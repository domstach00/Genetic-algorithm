from make_graph.graph import *
from algorithms.elitism import *
from algorithms.mutation import *
from algorithms.selection import *
from algorithms.crossover import *
from make_graph.observation import *
import CONSTANTS



class GeneticAlgorithm:
    pop_size = CONSTANTS.GA_POP_SIZE
    is_elitism_on: bool = CONSTANTS.ELITISM_IS_ON

    def __init__(self, config: Config):
        self.config = config
        self.list_of_observations = []
        self.current_iteration = 0
        self.iteration_limit = CONSTANTS.GA_ITERATIONS
        self.population: 'list[Individual]' = []
        self.finished = False
        self.elitism_alg = Elitism()
        self.cross_alg = Crossover()
        self.mutation_alg = Mutation()
        if CONSTANTS.GA_SELECTION == 0:
            self.selection_alg = RouletteSelection
        else:
            self.selection_alg = TournamentSelection


    def initialise(self):
        new_population = []
        for _ in range(self.pop_size):
            new_elem = Individual(self.config)
            new_elem.shuffle()
            new_elem.calc_score()
            new_population.append(new_elem)
        self.population = new_population

    def run(self):
        self.__notify()
        for _ in range(self.iteration_limit):
            self.run_iteration()
            self.__notify()
            self.current_iteration += 1
        self.finished = True
        self.__notify()


    def run_iteration(self):
        # SELECT ELITES
        self.population = sorted(self.population)
        if self.is_elitism_on:
            self.elitism_alg.get_elite_copies(self.population)

        # PARENT SELECTION
        parent1, parent2 = self.selection_alg.select(self.population)

        # CROSSOVER
        if random.random() <= CONSTANTS.CROSSOVER_PX_PROBABILITY:
            child1, child2 = self.cross_alg.cross_parents_create_individuals(parent1, parent2)
        else:
            child1 = Individual.copy(parent1)
            child2 = Individual.copy(parent2)

        self.population[-1] = child1
        self.population[-2] = child2

        # MUTATION
        for elem in self.population:
            Mutation.change_individual(elem)

        # Calculate new scores for individuals in population
        for elem in self.population:
            elem.calc_score()

        self.population = sorted(self.population)
        if self.is_elitism_on:
            for i in range(1, self.elitism_alg.elite_count + 1):
                self.population[-i] = self.elitism_alg.elites[i-1]
            self.population = sorted(self.population)


    def __notify(self):
        self.list_of_observations.append(Observation(self.population))
        best = [0, 0, 0, 0, 0]
        for i in range(5):
            best[i] = self.population[i].score

        print(f"Iteration:  {self.current_iteration}/{self.iteration_limit} | Top 5: {best}     | current best: {min(best)}")
        if self.finished:
            print(f"Best setup: {self.population[0].list}")
            graph = Graph(self.list_of_observations, self.config)
            graph.make_graph()



