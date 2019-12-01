from Knapsack import Knapsack
from time import time

def test_hamming_distance_one():

    input = ['0', '1', '00','11','101','1101','000000000000000000000000000000000','000000000000100001000000000000010']
    result = [
        ['1'],
        ['0'],
        ['10','01'],
        ['01','10'],
        ['001','111','100'],
        ['0101','1001','1111','1100']
        ]
    avg = 0.0

    iters = 100
    for i in range(iters):
        t1 = time()
        for i in range(len(input)):
            knap = Knapsack(num_objects=len(input[i]))
            knap.hamming_distance(input[i],distance=5)
        t2 = time()
        diff = t2-t1
        avg+=diff
    
    avg = avg / iters
    print("Average " + str(avg))
   
#test_hamming_distance_one()

var = [0 for i in range(10)]
print(var)

t1 = time()
knap = Knapsack(num_objects=len(var))
print(knap.hamming_distance_onev2(var,distance=6))
t2 = time()

print("New function " + str(t2-t1))


t1 = time()
knap = Knapsack(num_objects=len(var))
print(knap.hamming_distance_one(var))
t2 = time()

print("Old function " + str(t2-t1))