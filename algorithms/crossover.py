from lab1_Dominik_Stachowiak import *
import random
import CONSTANTS


class Crossover:
    Px_probability = CONSTANTS.CROSSOVER_PX_PROBABILITY

    def __init__(self, parent_1: Individual, parent_2: Individual):
        if len(parent_1.list) != len(parent_2.list):
            print(f"Parents list len is not the same p1: {len(parent_1.list)}, p2: {len(parent_1.list)}")
            return
        self.parent_1: Individual = parent_1
        self.parent_2: Individual = parent_2
        self.cross_point: int = self.__choose_point()

    '''Create point where to seperate parents'''
    def __choose_point(self):
        return random.randrange(1, len(self.parent_1.list))

    '''Create children only as a lists'''
    def cross_parents(self) -> (list, list):
        # Probability check
        if random.random() < self.Px_probability:
            return

        # Create dictionaries
        used_p1: dict = self.create_dictionary()
        used_p2: dict = self.reverse_dictionary(used_p1)

        # Create children
        child_1 = self.sex(self.parent_1, used_p1, used_p2)
        child_2 = self.sex(self.parent_2, used_p2, used_p1)

        # Show resoult
        print(self.cross_point)
        print(child_1)
        print(child_2)

        return child_1, child_2

    '''Create children as individuals and calculate score'''
    def cross_parents_create_individuals(self) -> (Individual, Individual):
        child_1, child_2 = self.cross_parents()

        child_individual_1 = Individual(self.parent_1.config)
        child_individual_2 = Individual(self.parent_2.config)

        child_individual_1.list = child_1
        child_individual_2.list = child_2

        child_individual_1.calc_score()
        child_individual_2.calc_score()

        return child_individual_1, child_individual_2

    '''Make dictionary until the cross_point is reached'''
    def create_dictionary(self) -> dict:
        dictionary = {}
        for elem_1, elem_2, elem_number in zip(self.parent_1.list, self.parent_2.list, range(len(self.parent_1.list))):
            if self.cross_point > elem_number:
                dictionary[elem_1] = elem_2
            else:
                break
        return dictionary

    def reverse_dictionary(self, dictionary: dict) -> dict:
        reverse_dictionary = {v: k for k, v in dictionary.items()}
        return reverse_dictionary

    '''Cross the parents to make child and fix it if necessary'''
    def sex(self, p_1, dictionary, reverse_dictionary):
        child = []
        for elem_1, elem_number in zip(p_1.list, range(len(p_1.list))):
            if elem_number < self.cross_point and elem_1 in dictionary:
                child.append(dictionary[elem_1])
            elif elem_number > self.cross_point and elem_1 in reverse_dictionary:
                # Here we make a fix if the moved element is already in list,
                # then we just use reverse dictionary to give a correct value
                child.append(reverse_dictionary[elem_1])
            else:
                child.append(elem_1)
        return child
