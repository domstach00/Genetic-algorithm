from individual import *
import random
import CONSTANTS


def reverse_dictionary_odl(dictionary: dict) -> dict:
    # print(dictionary.values())
    # reverse_dictionary = {v: k for k, v in dictionary.items()}
    reverse_dictionary = {}
    for k, v in dictionary.items():
        reverse_dictionary[v] = dictionary.get(v, []) + [k]
    return reverse_dictionary


class Crossover:
    """Create point where to seperate parents"""
    def __choose_point(self):
        return random.randrange(1, len(self.parent_1.list))

    '''Create children only as a lists'''
    def cross_parents_TUTAJ(self) -> (list, list):
        # Create dictionaries
        used_p1, used_p2 = self.create_dictionary()


        # Create children
        child_1 = self.__cross_parents(self.parent_1, used_p1, used_p2)
        child_2 = self.__cross_parents(self.parent_2, used_p2, used_p1)

        return child_1, child_2

    '''Create children as individuals and calculate score'''
    def cross_parents_create_individuals(self, parent_1: Individual, parent_2: Individual) -> (Individual, Individual):
        self.parent_1 = parent_1
        self.parent_2 = parent_2
        self.cross_point = self.__choose_point()

        child_1, child_2 = self.cross_parents_TUTAJ()

        child_individual_1 = Individual(self.parent_1.config)
        child_individual_2 = Individual(self.parent_2.config)

        child_individual_1.list = child_1
        child_individual_2.list = child_2

        child_individual_1.calc_score()
        child_individual_2.calc_score()

        return child_individual_1, child_individual_2

    '''Make dictionary until the cross_point is reached'''
    def create_dictionary(self):
        dictionary = {}
        reverse_dictionary = {}
        for elem_1, elem_2, elem_number in zip(self.parent_1.list, self.parent_2.list, range(len(self.parent_1.list))):
            if self.cross_point > elem_number:
                dictionary[elem_1] = elem_2
            else:
                break
        return dictionary, reverse_dictionary

    '''Cross the parents to make child and fix it if necessary'''
    def __cross_parents(self, p_1: Individual, dictionary: dict, reverse_dictionary: dict) -> list:
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
