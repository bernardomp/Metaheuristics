from Knapsack import Knapsack
from generalVNS import GeneralVNS
from reducedVNS import ReducedVNS
from basicVNS import BasicVNS
 
def main():
    
    

    knap = Knapsack()
    knap.read_values("input/input2.txt")
    knap.gen_neighbour_structures()


    x = [GeneralVNS(knap).solve(seed=i)[1] for i in range(100)]

    print(sum(x)/100)
if __name__ == "__main__":
    main()