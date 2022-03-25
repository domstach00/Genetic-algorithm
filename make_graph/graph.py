from genetic_algorithm import *
from make_graph.observation import *
from CONSTANTS import *
import matplotlib.pyplot as plt


class Graph:
    graph_number = 1
    graph_style = GRAPH_STYLE

    def __init__(self, list_of_observations: 'list[Observation]', config: Config):
        self.list_of_observations: 'list[Observation]' = list_of_observations
        self.line_best, self.line_worst, self.line_avg = self.__get_data_from_observers()
        self.field_graph = list(range(0, len(list_of_observations)))

    '''Make lists of best and worsts values in populations'''
    def __get_data_from_observers(self) -> (list[int], list[int], list):
        best = []
        worst = []
        avg = []
        for elem in self.list_of_observations:
            best.append(elem.best_value)
            worst.append(elem.worst_value)
            avg.append(elem.avg_value)
        return best, worst, avg

    def __get_details(self) -> str:
        text = f"Px: {CROSSOVER_PX_PROBABILITY}, Pm: {MUTATION_PM_PROBABILITY}, \n" \
               f"Tournament size: {SELECTION_TOURNAMENT_BATCH_SIZE}, \nIs elite on: {ELITISM_IS_ON}"
        if ELITISM_IS_ON:
            text += f", Elitism size: {ELITISM_LIST_SIZE}"
        text += f"\nGA population: {GA_POP_SIZE}, Iterations: {GA_ITERATIONS}, \n" \
                f"Selection type: {SELECTION_NAME[GA_SELECTION]}"
        return text

    def make_graph(self):
        graph_name = f"Graph nr_{self.graph_number}"
        plt.title(graph_name)
        plt.figtext(.15, .76, self.__get_details())
        plt.style.use(self.graph_style)
        plt.plot(self.field_graph, self.line_best, label="Best value", color=GRAPH_COLORS['best'])
        plt.plot(self.field_graph, self.line_avg, label="Average value", color=GRAPH_COLORS['average'])
        plt.plot(self.field_graph, self.line_worst,  label="Worst value", color=GRAPH_COLORS['worst'])
        plt.xlabel('Iteration')
        plt.ylabel('Score')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        if GRAPH_SAVE:
            plt.savefig(f"{graph_name}.png")
        plt.show()
        self.graph_number += 1


