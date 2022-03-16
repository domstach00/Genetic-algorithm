import random

from data import Config

class Individual:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.array: list[int] = []
        self.score: int = None
    
    def shuffle(self):
        machines = list(range(self.config.width * self.config.height)) # Tworzymy liste o długości width x height
        random.shuffle(machines) # Shufflujemy ją
        self.array = machines[0:self.config.machine_count] # Wybieramy tylko elementy od 0 do ilosci maszyn 'machine_count'

    def calculate_score(self):
        score = 0
        connections = self.config.connections
        for key in connections:
            for value in connections[key]: # Dla kazdego polaczenia bierzemy key = source i value = destination 
                cost = self.config.costs[(key, value)] # Odszukujemy cost dla danego polaczenia
                flow = self.config.flows[(key, value)] # Tak samo z flow
                
                source_position = self.array[key] # Sprawdzamy pozycje maszyny od
                dest_position = self.array[value] # Sprawdzamy pozycje maszyny do
                # Obliczamy wartosc funkcji przystosowania
                score += cost * flow * \
                    (abs(source_position % self.config.width - dest_position % self.config.width) + \
                    abs(source_position // self.config.height - dest_position // self.config.height))
        self.score = score
        return score