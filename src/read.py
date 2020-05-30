import csv
import time

from src.Knapsack import Knapsack
from src.multistart import VnsMultistart

ALGORITHM_REPEATS = 30
FILE_OUTPUT = "v2.csv"

for algorithm in ["GeneralVNS", "BasicVNS", "ReducedVNS"]:
    print("Starting " + str(algorithm))

    csvfile = open('output/' + algorithm + FILE_OUTPUT, 'a')  # creating  a csv writer object

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Testcase", "Algorithm", "Repeats", "Min_value", "Mean_value", "Max_value", "Time_per_iter"])

    with open("input/inputs.txt", "r") as f:

        test_cases = int(next(f).split(" ")[0])

        for test_case in range(1, test_cases + 1):

            next(f)
            elements, capacity = map(int, next(f).split(" "))

            values = list(map(float, next(f).split(" ")))
            if len(values) != elements:
                print("Number of values greater than expected")

            weights = list(map(float, next(f).split(" ")))
            if len(weights) != elements:
                print("Number of weights greater than expected")

            knap = Knapsack(elements, capacity, values, weights)

            vns_algorithm = globals()[algorithm](knap)
            x = VnsMultistart(ALGORITHM_REPEATS, vns_algorithm)

            print("Testcase " + str(test_case) + "/" + str(test_cases) + " for " + algorithm)
            begin_time = time.time()
            sol = x.solve()
            end_time = time.time()
            print(" -----> Solved in " + str(end_time - begin_time) + " seconds")

            csvwriter.writerow(
                [test_case, algorithm, ALGORITHM_REPEATS, min(sol[1]), sum(sol[1]) / ALGORITHM_REPEATS, max(sol[1]),
                 (end_time - begin_time) / ALGORITHM_REPEATS])

    csvfile.close()