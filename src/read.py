from Knapsack import Knapsack
from multistart import VNS_MUltistart
from reducedVNS import ReducedVNS

algorithm_repeteats = 1

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

    
        x = VNS_MUltistart(algorithm_repeteats,ReducedVNS(knap))
        sol = x.solve()
        print("Test " + str(test_case) + ": " + str(sum(sol[1])/algorithm_repeteats))

