import json


class Point:
    def __init__(self, source, dest, cost=None, flow=None):
        self.cost = cost
        self.flow = flow
        self.source = source
        self.dest = dest

    def set_cost(self, cost):
        self.cost = cost

    def set_flow(self, flow):
        self.flow = flow


class FLO:
    def __init__(self, row_nr: int, column_nr: int):
        self.row_nr = row_nr
        self.column_nr = column_nr

    def read(self, json_file_cost, json_file_flow):
        objs = []
        file_cost = json.load(open(json_file_cost))
        file_flow = json.load(open(json_file_flow))

        for i in file_cost:
            objs.append(Point(i['source'], i['dest'], cost=i['cost']))

        for i in objs:
            for j in file_flow:
                if i.source == j['source'] and i.dest == j['dest']:
                    i.set_flow(j['amount'])
                    break
        self.obj_from_file = objs
        for i in objs:
            print(i.source, i.dest, i.cost, i.flow)


    def manhattan_distance(self, row_i, col_i, row_j, col_j):
        return abs(row_i - row_j) + abs(col_i - col_j)

    def adaptation_function(self):
        sum = 0
        for i in range(self.row_nr):
            for j in range(self.column_nr):



if __name__ == '__main__':
    ob = FLO(3, 3)
    ob.read('easy_cost.json', 'easy_flow.json')
