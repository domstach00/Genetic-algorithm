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

    '''Start algorithm'''
    def run(self):
        self.__notify()
        for _ in range(self.iteration_limit):
            self.run_iteration()
            self.__notify()
            self.current_iteration += 1
        self.finished = True
        self.__notify()

    def run_iteration(self):
        self.population = sorted(self.population)
        # SELECT ELITES
        if self.is_elitism_on:
            self.elitism_alg.get_elite_copies(self.population)

        # PARENT SELECTION
        parent1, parent2 = self.selection_alg.select(self.population)

        # CROSSOVER
        if random.random() <= CONSTANTS.CROSSOVER_PX_PROBABILITY:
            child1, child2 = self.cross_alg.cross(parent1, parent1)
            space_for_elites = 0
            # If elitism is on we save the worsts individual to replace them with elites
            if self.is_elitism_on:
                space_for_elites = self.elitism_alg.elite_count

            # Way of replace individual with a new child
            if CONSTANTS.CHILD_REPLACE[CONSTANTS.GA_CHILD_REPLACE_WORST]:
                # Here we replace parent with a child
                self.population[self.population.index(parent1)] = child1
                self.population[self.population.index(parent2)] = child2
            else:
                # Here we replace child with the worst element
                self.population[-1 - space_for_elites] = child1
                self.population[-2 - space_for_elites] = child2

        # MUTATION
        if random.random() <= CONSTANTS.MUTATION_PM_PROBABILITY:
            for elem in self.population:
                Mutation.change_individual(elem)

        # Calculate new scores for individuals in population
        for elem in self.population:
            elem.calc_score()

        # Replace the worst individuals with elites
        if self.is_elitism_on:
            self.population = sorted(self.population)
            for i in range(1, self.elitism_alg.elite_count + 1):
                self.population[-i] = self.elitism_alg.elites[i-1]

    '''Save a view of new population in observer to make a plot when GA is finished'''
    def __notify(self):
        self.list_of_observations.append(Observation(self.population))
        best = [0, 0, 0, 0, 0]
        for i in range(5):
            best[i] = self.population[i].score

        if CONSTANTS.CONSOLE_PRINT_ITERATIONS:
            print(f"Iteration:  {self.current_iteration}/{self.iteration_limit} | Top 5: {best}     | current best: {min(best)}")
        if self.finished:
            if CONSTANTS.CONSOLE_PRINT_LAST_ITERATION:
                print(
                    f"Last iteration:  {self.current_iteration}/{self.iteration_limit} | Top 5: {best}     "
                    f"| current best: {min(best)}")
            if CONSTANTS.CONSOLE_PRINT_BEST_SETUP:
                print(f"Best setup: {self.population[0].list}")
            graph = Graph(self.list_of_observations, self.config)
            graph.make_graph()
