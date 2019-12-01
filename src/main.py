from Knapsack import Knapsack
from generalVNS import GeneralVNS
from reducedVNS import ReducedVNS
from basicVNS import BasicVNS

def main():
    
    knap = Knapsack()
    knap.read_values("input/input2.txt")
    knap.gen_neighbour_structures()
   

    reduced = BasicVNS(knap,seed=0)
    print("SOLVING")
    x = reduced.solve()
    print(x)

if __name__ == "__main__":
    main()