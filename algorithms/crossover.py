from individual import *
import random
import CONSTANTS


class Crossover:

    """Cross parents to make and return 2 children"""
    def cross(self, parent1: Individual, parent2: Individual):
        self.p1 = Individual.copy(parent1)
        self.p2 = Individual.copy(parent2)
        cut_point = random.randint(0, len(parent1.list))
        used = {}
        used_reversed = {}
        for i in range(cut_point):
            old = self.p1.list[i]
            new = self.p2.list[i]

            if new not in used_reversed and old not in used:
                used[new] = old
                used_reversed[old] = new
            elif new in used_reversed and old in used:
                used[used_reversed[new]] = used[old]
                used_reversed[used[old]] = used_reversed[new]
                used.pop(old)
                used_reversed.pop(new)
            elif new in used_reversed:
                used_reversed[old] = used_reversed[new]
                used[used_reversed[new]] = old
                used_reversed.pop(new)
            else:
                used[new] = used[old]
                used_reversed[used[new]] = old
                used.pop(old)

            self.p1.list[i] = new
            self.p2.list[i] = old


        for i in range(cut_point, len(self.p1.list)):
            self_gen = self.p1.list[i]
            if self_gen in used:
                self.p1.list[i] = used[self_gen]

            other_gen = self.p1.list[i]
            if other_gen in used_reversed:
                self.p2.list[i] = used_reversed[other_gen]

        self.p1.calc_score()
        self.p2.calc_score()

        return self.p1, self.p2
