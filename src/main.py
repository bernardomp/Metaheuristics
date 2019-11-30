from reducedVNS import ReducedVNS
from basicVNS import BasicVNS
from generalVNS import GeneralVNS
from Knapsack import Knapsack

def main():
    
    knap = Knapsack()
    knap.read_values("input/input1.txt")
    knap.gen_neighbour_structures()


    reduced = GeneralVNS(knap,seed=1)
    x = reduced.solve()
    print(x)


if __name__ == "__main__":
    main()