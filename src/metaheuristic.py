import argparse
import csv
import time

from Knapsack import Knapsack
from multistart import VnsMultistart

example_text = "Example: python3 metaheuristic 30 input/inputs.txt ./ BasicVNS ReducedVNS"
parser = argparse.ArgumentParser(epilog=example_text)
parser.add_argument("repeats", help="number of repeats for each algorithm", type=int)
parser.add_argument("input", help="filepath containing the input data", type=str)
parser.add_argument("output", help="filepath containing the output data", type=str)
parser.add_argument("algorithms", help="list of algorithms: ReducedVNS, BasicVNS or GeneralVNS", type=str, nargs="+")
args = parser.parse_args()

ALGORITHM_REPEATS = args.repeats
FILE_INPUT = args.input
FILE_OUTPUT = args.output
ALGORITHMS = args.algorithms

for algorithm in ALGORITHMS:
    print("Starting " + str(algorithm))

    csvfile = open(FILE_OUTPUT + algorithm + ".csv", 'a')  # creating  a csv writer object

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Testcase", "Algorithm", "Repeats", "Min_value", "Mean_value", "Max_value", "Time_per_iter"])
    csvfile.flush()
    with open(FILE_INPUT, "r") as f:

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
            csvfile.flush()

    csvfile.close()
