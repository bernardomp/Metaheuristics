from itertools import combinations

import numpy as np


class Knapsack:
    """
    Defines a class for the Knapsack problem
        Args:
            num_objects (int): The amount of objects stated in the problem
            capacity (int): The knapsack capacity
            values (array): An array storing the value of each object
            weights (array): An array storing the weight of each object
    """

    def __init__(self, num_objects: int = None, capacity: int = None, values: list = None, weights: list = None):
        self.num_objects = num_objects
        self.capacity = capacity
        self.values = values
        self.weights = weights

    def read_values(self, filename: str):
        """
        Args:
            filename (object):

        """
        file = open(filename, "r")
        lines = file.readlines()

        aux = list(map(int, lines[0].split(" ")))

        self.num_objects = aux[0]
        self.capacity = aux[1]

        self.values = list(map(float, lines[1].split(" ")))
        self.weights = list(map(float, lines[2].split(" ")))

    def gen_neighbourhood(self, x: list = None, distance: int = 1) -> list:
        potential_neighbours = self.hamming_distance(x, distance)

        return list(filter(self.feasible_solution, potential_neighbours))

    def __str__(self):
        return "Capacity: " + str(self.capacity) + "\n" + \
               "Objects: " + str(self.num_objects) + "\n" + \
               "Values: " + str(self.values) + "\n" + \
               "Weights: " + str(self.weights)

    def evaluation_function(self, x: list) -> float:
        """
        Computes the fitness or value of a given solution x
        Args:
            x (str): The binary string to be checked
        """
        value = 0

        for index in range(self.num_objects):

            if x[index] == 1:
                value += self.values[index]

        return value

    def feasible_solution(self, x: list) -> bool:
        """
        Checks if the solution x fulfill the problem constraints
        Args:
            x (str): The binary string to be checked
        """
        weight = 0

        for index in range(self.num_objects):

            if x[index] == 1:
                weight += self.weights[index]

                if weight > self.capacity:
                    return False

        return True

    def hamming_distance(self, x: list, distance: int = 1):
        '''
        Given a solution x (represented as a binary string) generates other solutions x1, x2, ..., xn whose
        hamming distance respect to x is distance.
            Args:
                distance:
                x (str): A solution of the problem
            Returns
                An array of solutions with hamming distance 1 respect to x
        '''

        combs = combinations(range(self.num_objects), distance)

        return np.array([self.flip_bits(x, positions=comb) for comb in combs])

    @staticmethod
    def flip_bits(x: list, positions: list):

        aux = np.copy(x)

        for pos in positions:
            aux[pos] = 1 - aux[pos]

        return aux
