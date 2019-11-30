import pytest
import sys
from src.Knapsack import *


def test_hamming_distance_one():

    input = ['0', '1', '00','11','101','1101']
    result = [
        ['1'],
        ['0'],
        ['10','01'],
        ['01','10'],
        ['001','111','100'],
        ['0101','1001','1111','1100']
        ]

    for i in range(len(input)):
        knap = Knapsack(num_objects=len(input[i]))
        assert knap.hamming_distance_one(input[i]) == result[i]


def test_hamming_distance():

    tests = [
        ("111",2,set(['011','101','110','001','010','100']) ),
        ("0000",3, set(['1000','0100','0010','0001','1100','1010','1001','0110','0101','0011','1110','1101','1011','0111']))
    ]

    for test in tests:
        knap = Knapsack(num_objects=len(test[0]))
        assert knap.hamming_distance(test[0],test[1]) == test[2]
   

def test_evaluation_function():

    tests = [
        ("111",3, [15,15,15],45),
        ("000",3, [15,15,15],0),
        ("10",2, [5,2],5),
        ("1011",4, [5,2,6,9],20),
    ]

    for test in tests:
        knap = Knapsack(num_objects=test[1],values=test[2])
        assert knap.evaluation_function(test[0]) == test[3]

def test_feasible_function():

    tests = [
        ("111",3,20, [15,15,15],False),
        ("000",3,20, [15,15,15],True),
        ("10",2,0, [5,2],False),
        ("1011",4,15, [5,2,6,4],True)
    ]

    for test in tests:
        knap = Knapsack(num_objects=test[1],weights=test[3],capacity=test[2])
        assert knap.feasible_solution(test[0]) == test[4]


def test_gen_neighbourhood():
    
    tests = [
        # (#solution,#num_objects,#capacity,#hamming_distance,#objects,#result)
        ("000",3,20,1,[15,15,15],{"100","010","001"}),
        ("1011",4,15,1, [5,2,6,4],{"0011","1001","1010"}),
        ("1000",4,10,2, [1,2,8,3],{"0000","1100","1010","1001", "0100","0010","0001", "1101"})
    ]

    for test in tests:
        knap = Knapsack(num_objects=test[1],capacity=test[2],weights=test[4])
        assert set(knap.gen_neighbourhood(test[0],distance=test[3])) == test[5]
