from Knapsack import Knapsack
from multistart import VNS_Multistart
from algorithms.reducedVNS import ReducedVNS
from algorithms.basicVNS import BasicVNS
from algorithms.generalVNS import GeneralVNS
import time,csv

algorithms_repeats = 1

csvfile = open('output/result.csv','w')
#creating  a csv writer object
csvwriter = csv.writer(csvfile)
csvwriter.writerow(["Testcase", "Algorithm", "Repeats", "Min_value", "Mean_value", "Max_value", "Time_per_iter"])

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

        #Testcase, Algorithm, Repeats, Min_value, Mean_value, Max_value, Time_per_iter

        for algorithm in ["ReducedVNS"]:# "BasicVNS", "GeneralVNS"]:

            vns_algorithm = globals()[algorithm](knap)
            x = VNS_Multistart(algorithms_repeats,vns_algorithm)

            begin_time = time.time()
            sol = x.solve()
            end_time = time.time()

            csvwriter.writerow([test_case, algorithm, algorithms_repeats, min(sol[1]), sum(sol[1])/algorithms_repeats, max(sol[1]), (end_time-begin_time)/algorithms_repeats])


csvfile.close()