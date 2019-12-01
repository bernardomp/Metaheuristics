from src.reducedVNS import ReducedVNS
from src.basicVNS import BasicVNS
from src.generalVNS import GeneralVNS
from src.Knapsack import Knapsack

def main():
    
    knap = Knapsack()
    knap.read_values("input/input3.txt")
    knap.gen_neighbour_structures()


    reduced = GeneralVNS(knap,seed=0)
    print("SOLVING")
    x = reduced.solve()
    print(x)

if __name__ == "__main__":
    main()