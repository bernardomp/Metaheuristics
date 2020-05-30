import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from Knapsack import Knapsack
from algorithms.VNS import VNS


def test_shakes():
    knap = Knapsack()
    knap.read_values("input/input1.txt")

    vns = VNS(knap)

    tests = [
        ([0, 0, 0, 0, 0, 0],
         [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 1]]),
        ([0, 0, 0, 1, 0, 0],
         [[1, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0],
          [0, 0, 0, 1, 0, 1]]),
        ([0, 0, 0, 0, 1, 1],
         [[1, 0, 0, 0, 1, 1], [0, 1, 0, 0, 1, 1], [0, 0, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 1, 0]])
    ]

    for test in tests:
        assert vns.shake(test[0]).tolist() in test[1]