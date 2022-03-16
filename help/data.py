import json

class Config:
    def __init__(self, width: int, height: int, machine_count: int, filepath_cost: str, filepath_flow: str) -> None:
        self.width: int = width
        self.height: int = height
        self.machine_count: int = machine_count
        self.connections: dict[int, list[int]] = {}
        self.costs: dict[(int,int), int] = {}
        self.flows: dict[(int,int), int] = {}
        self.read_data(filepath_cost, filepath_flow)

    def read_data(self, filepath_cost, filepath_flow):
        with open(filepath_cost) as costfile:
            cost_temp = json.load(costfile)
        with open(filepath_flow) as flowfile:
            flows_temp = json.load(flowfile)

        for cost in cost_temp:
            self.costs[(cost["source"], cost["dest"])] = cost["cost"]
            if cost["source"] in self.connections:
                self.connections[cost["source"]].append(cost["dest"])
            else:
                self.connections[cost["source"]] = [cost["dest"]]
        
        for flow in flows_temp:
            self.flows[(flow["source"], flow["dest"])] = flow["amount"]
        
