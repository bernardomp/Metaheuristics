from typing import Tuple

import numpy as np


class VNS:
    """
    Base class for the implementation of the VNS algorithms
    """

    def __init__(self, problem):

        self.problem = problem
        self.evaluation_function = self.problem.evaluation_function

        # Reset neighbour structure to the first structure
        self.k = 1

        # Defines the maximum number of neighbourhood structures
        self.k_max = 5

    def gen_initial_solution(self) -> list:
        """
        Generates an initial solution
        """

        initial_sol = np.random.randint(2, size=self.problem.num_objects)

        while not self.problem.feasible_solution(initial_sol):
            initial_sol = np.random.randint(2, size=self.problem.num_objects)

        return initial_sol

    def shake(self, x_cur: list) -> list:
        """
        Generates randomly a neighbour solution of another solution x_cur given a neighbour structure n
            Args:
                x_cur : A problem solution
        """

        neighbours = self.problem.gen_neighbourhood(x=x_cur, distance=self.k)
        element = np.random.choice(np.arange(len(neighbours)))

        return neighbours[element]

    def neighbourhood_change_sequential(self, x_cur: list, x_new: list, k: int) -> Tuple[list, int]:
        """
         If an improvement of the current solution in some neighborhood structure occurs, the search is resumed
         in the first neighborhood structure of the new solution, otherwise the search is continued in the next neighborhood
        Args:
            x_cur: Current solution
            x_new: Potential new solution
            k: Index to the neighbourhood structure

        Returns:
            The best solution and index to the new neighbourhood structure
        """
        x_aux = None

        if self.evaluation_function(x_cur) < self.evaluation_function(x_new):
            x_aux = x_new
            k = 1
        else:
            k += 1
            x_aux = x_cur

        return x_aux, k

    def solve(self, seed: int = 0):
        np.random.seed(seed)
