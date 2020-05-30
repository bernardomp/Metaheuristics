import pytest, sys,os, numpy
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from Knapsack import Knapsack
from algorithms.basicVNS import BasicVNS

def test_solve():
    knap = Knapsack()
    knap.read_values("input/input1.txt")
    

    basic = BasicVNS(knap)
    x = basic.solve(seed=5)
    print(x)
    assert x[0].tolist() == [0, 1, 1, 0, 0, 1]
    assert x[1] == 3800