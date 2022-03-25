import json

class Config:
    def __init__(self, width: int, height: int, machine_count: int):
        self.width = width
        self.height = height
        self.machine_count = machine_count
        self.costs: 'dict[(int, int), int]' = {}
        self.flows: 'dict[(int, int), int]' = {}
        self.connections: 'dict[int, list[int]]' = {}     # [source, <lista destynacji do których trzeba się połączyć z tanego źródła>]

    def load_data(self, level: str):
        file_costs = f'dane/{level}_cost.json'
        file_flows = f'dane/{level}_flow.json'

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
