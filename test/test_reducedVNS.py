import pytest
import sys
from src.Knapsack import *
from src.reducedVNS import *

def test_shake():
    knap = Knapsack()
    knap.read_values("input/input1.txt")
    knap.gen_neighbour_structures()

    reduced = ReducedVNS(knap,seed=0)

    tests = [
        ("000000",["100000","010000","001000","000100","000010","000001"]),
        ("000100",["100100","010100","001100","000000"]),
        ("000011",["100011","010011","001011","000001","000010"]),
    ]
    
    for test in tests:

        assert reduced.shake(test[0]) in test[1]
