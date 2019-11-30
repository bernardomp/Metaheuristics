from functools import reduce
import random
from vns import VNS

class BasicVNS(VNS):
    
    def improvement_function(self,x_cur):

        neighbourhood_structure = self.N[self.k]
        neighbours = list(neighbourhood_structure(x_cur))

        return max(neighbours,key=self.evaluation_function)


    def solve(self):

        x = self.gen_initial_solution()
        print("Initial solution: " + str(x) + " -----> Value: " + str(self.evaluation_function(x)))

        for i in range(5):
            print("Iteration " + str(i))
            self.k = 0
            while self.k<self.k_max:
                x_new = self.shake(x)
                x_local = self.improvement_function(x_new)
                x = self.neighbourhood_change_sequential(x,x_local)
        
        print("Best solution: " + str(x) + " -----> Value: " + str(self.evaluation_function(x)))
        return x


   
        