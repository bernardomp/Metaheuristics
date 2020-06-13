import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from Knapsack import Knapsack
from algorithms.reducedVNS import ReducedVNS


def test_solve():
    INPUT_FILE = "test/testing_files/input1.txt"
    knap = Knapsack()
    knap.read_values(INPUT_FILE)

    reduced = ReducedVNS(knap)
    x = reduced.solve(seed=1)
    print(x)
    assert x[0].tolist() == [1,1,1,0,0,1]