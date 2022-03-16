import json
import random


class Config:
    def __init__(self, width: int, height: int, machine_count: int):
        self.width = width
        self.height = height
        self.machine_count = machine_count
        self.costs: dict[(int, int), int] = {}
        self.flows: dict[(int, int), int] = {}
        self.connections: dict[int, list[int]] = {}     # [source, <lista destynacji do których trzeba się połączyć z tanego źródła>]

    def load_data(self, file_costs: str, file_flows: str):
        with open(file_flows) as file_flows:
            flows = json.load(file_flows)
        with open(file_costs) as costs_file:
            costs = json.load(costs_file)

        for cost in costs:
            self.costs[(cost["source"], cost["dest"])] = cost["cost"]
            if cost["source"] in self.connections:
                self.connections[cost["source"]].append(cost["dest"])
            else:
                self.connections[cost["source"]] = [cost["dest"]]

        for flow in flows:
            self.flows[(flow["source"], flow["dest"])] = flow["amount"]



class Adaptation_funcion:
    def __init__(self, config: Config):
        self.config: Config = config
        self.list: list[int] = list(range(self.config.width * self.config.height))
        self.score: int = None

    '''Metoda losowa'''
    def shuffle(self, list):
        random.shuffle(list)    # Losowo przestawiamy pozycje na liscie
        self.list = list[0:self.config.machine_count]   # Wybieramy dokładnie tyle losowych pozycji ile maszyn mamy do rozmieszczenia

    '''Obliczenie funkcji przystosowania'''
    def calc_score(self):
        score = 0
        connections = self.config.connections
        for source in connections:
            for dest in connections[source]:
                # Odczytywanie cost i flow dla każdego połączenia
                cost = self.config.costs[(source, dest)]
                flow = self.config.flows[(source, dest)]

                # Obliczanie funkcji przystosowania
                score += cost * flow * self.calc_manhattan(self.list[source], self.list[dest])
        self.score = score

    '''Liczenie odległości Manhattan'''
    def calc_manhattan(self, source: int, dest: int) -> int:
        x = abs(source % self.config.width - dest % self.config.width)
        y = abs(source // self.config.height - dest // self.config.height)
        return x + y


if __name__ == '__main__':
    # Ustawienie konfuguracji wstępnej
    config = Config(3, 3, 9)
    config.load_data('dane/easy_cost.json', 'dane/easy_flow.json')

    adaptation_f = Adaptation_funcion(config)
    print("Pierwotny wygląd listy:", adaptation_f.list)
    adaptation_f.shuffle(adaptation_f.list)  # tasujemy liste
    print("Lista po przetasowaniu:", adaptation_f.list)
    adaptation_f.calc_score()
    print("Wynik funkcji przystosowania:", adaptation_f.score)
