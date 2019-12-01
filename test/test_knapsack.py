import pytest
import sys
from ..src.Knapsack import *

def test_hamming_distance():

    tests = [
        ([1,0,1,0],1,[[0,0,1,0],[1,1,1,0],[1,0,0,0],[1,0,1,1]]),
        ([1,1,1],2,[[0,0,1],[0,1,0],[1,0,0]]),
        ([0,0,0,0],3, [ [1,1,1,0],[1,1,0,1],[1,0,1,1],[0,1,1,1]])
    ]

    for test in tests:
        knap = Knapsack(num_objects=len(test[0]))
        assert sorted(knap.hamming_distance(test[0],test[1])) == sorted(test[2])
   

def test_evaluation_function():

    tests = [
        ([1,1,1],3, [15,15,15],45),
        ([0,0,0],3, [15,15,15],0),
        ([1,0],2, [5,2],5),
        ([1,0,1,1],4, [5,2,6,9],20),
    ]

    for test in tests:
        knap = Knapsack(num_objects=test[1],values=test[2])
        assert knap.evaluation_function(test[0]) == test[3]

def test_feasible_function():

    tests = [
        ([1,1,1],3,20, [15,15,15],False),
        ([0,0,0],3,20, [15,15,15],True),
        ([1,0],2,0, [5,2],False),
        ([1,0,1,1],4,15, [5,2,6,4],True)
    ]

    for test in tests:
        knap = Knapsack(num_objects=test[1],weights=test[3],capacity=test[2])
        assert knap.feasible_solution(test[0]) == test[4]


def test_gen_neighbourhood():
    
    tests = [
        # (#solution,#num_objects,#capacity,#hamming_distance,#objects,#result)
        ([0,0,0],3,20,1,[15,15,15],[[1,0,0],[0,1,0],[0,0,1]]),
        ([1,0,1,1],4,15,1, [5,2,6,4],[[0,0,1,1],[1,0,0,1],[1,0,1,0]]),
        ([1,0,0,0],4,10,2, [1,2,8,3],[[0,1,0,0],[0,0,1,0],[0,0,0,1], [1,1,0,1]])
    ]

    for test in tests:
        knap = Knapsack(num_objects=test[1],capacity=test[2],weights=test[4])
        assert sorted(knap.gen_neighbourhood(test[0],distance=test[3])) == sorted(test[5])
