import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from algorithms.basicVNS import BasicVNS
from Knapsack import Knapsack

INPUT_FILE = "test/testing_files/input1.txt"

def test_solve():
    knap = Knapsack()
    knap.read_values(INPUT_FILE)

    basic = BasicVNS(knap)
    x = basic.solve(seed=5)
    print(x)
    assert x[0].tolist() == [0, 1, 1, 0, 0, 1]
    assert x[1] == 3800
