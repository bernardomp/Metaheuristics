import pytest
import sys
from Knapsack import Knapsack
from reducedVNS import ReducedVNS

def test_solve():
    knap = Knapsack()
    knap.read_values("input/input1.txt")
    knap.gen_neighbour_structures()


    reduced = ReducedVNS(knap,seed=1)
    x = reduced.solve()

    assert x == "111001" 