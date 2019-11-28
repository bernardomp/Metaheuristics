from Knapsack import Knapsack
from reducedVNS import ReducedVNS

def main():
    
    knap = Knapsack()
    knap.read_values("VNS/input/input1.txt")
    knap.neighbourhood_structure()
    print(knap.neighbourhood_structure[0])

    #print(ass("000"))

    #reduced = ReducedVNS(knap)

    #reduced.solve()

    print


if __name__ == "__main__":
    main()