import pytest
import sys,os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from Knapsack import Knapsack
from reducedVNS import ReducedVNS

def test_solve():
    knap = Knapsack()
    knap.read_values("input/input1.txt")
    knap.gen_neighbour_structures()


    reduced = ReducedVNS(knap,seed=1)
    x = reduced.solve()

    assert x == [1,1,1,0,0,1]