from Knapsack import Knapsack
from multistart import VNS_Multistart
from algorithms.reducedVNS import ReducedVNS
from algorithms.basicVNS import BasicVNS
from algorithms.generalVNS import GeneralVNS
import time

algorithms_repeats = 10

with open("input/inputs.txt","r") as f:

    test_cases = int(next(f).split(" ")[0])
    
    for test_case in range(1,test_cases+1):
    
        next(f)
        elements, capacity = map(int,next(f).split(" "))

        values = list(map(float,next(f).split(" ")))
        if len(values) != elements:
            print("Number of values greater than expected") 

        weights = list(map(float,next(f).split(" ")))
        if len(weights) != elements:
            print("Number of weights greater than expected") 
    
    
        knap = Knapsack(elements,capacity,values,weights)
        knap.gen_neighbour_structures()

    
        x = VNS_Multistart(algorithms_repeats,GeneralVNS(knap))

        begin_time = time.time()
        sol = x.solve()
        end_time = time.time()

        print("Test " + str(test_case) + ": Iterations: " + str(algorithms_repeats) + " --- Min: " + str(min(sol[1])) + " --- Mean: " + str(sum(sol[1])/algorithms_repeats) + " --- Max: " + str(max(sol[1])) + " --- Time per iteration: " + str((end_time-begin_time)/algorithms_repeats))

