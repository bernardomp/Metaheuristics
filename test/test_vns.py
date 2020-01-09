import pytest
import sys,os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from Knapsack import Knapsack
from algorithms.vns import VNS

def test_shakes():
    knap = Knapsack()
    knap.read_values("input/input1.txt")
    knap.gen_neighbour_structures()

    vns = VNS(knap)

    tests = [
        ([0,0,0,0,0,0],[[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]),
        ([0,0,0,1,0,0],[[1,0,0,1,0,0],[0,1,0,1,0,0],[0,0,1,1,0,0],[0,0,0,0,0,0],[0,0,0,1,1,0],[0,0,0,1,0,1]]),
        ([0,0,0,0,1,1],[[1,0,0,0,1,1],[0,1,0,0,1,1],[0,0,1,0,1,1],[0,0,0,1,1,1],[0,0,0,0,0,1],[0,0,0,0,1,0]])
    ]
    
    for test in tests:

        assert vns.shake(test[0]) in test[1]
