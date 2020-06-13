import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from Knapsack import Knapsack
from algorithms.generalVNS import GeneralVNS

INPUT_FILE = "test/testing_files/input1.txt"

def test_solve():
    knap = Knapsack()
    knap.read_values(INPUT_FILE)

    general = GeneralVNS(knap)
    x = general.solve(seed=1)

    assert x[0].tolist() == [1,1,1,0,0,1]