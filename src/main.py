from reducedVNS import ReducedVNS
from Knapsack import Knapsack

def main():
    
    knap = Knapsack()
    knap.read_values("input/input1.txt")
    knap.gen_neighbour_structure()
    print(knap.neighbour_structure[0])


    reduced = ReducedVNS(knap)

    x = reduced.solve()
    print(x)


if __name__ == "__main__":
    main()