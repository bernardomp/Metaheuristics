import pytest
import sys,os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from Knapsack import Knapsack
from algorithms.generalVNS import GeneralVNS

def test_solve():
    knap = Knapsack()
    knap.read_values("input/input1.txt")
    knap.gen_neighbour_structures()


    general = GeneralVNS(knap)
    x = general.solve(seed=1)

    assert x[0] == [1,1,1,0,0,1]