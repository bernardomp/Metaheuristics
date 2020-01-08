from functools import reduce
import random
from vns import VNS

class ReducedVNS(VNS):

    def solve(self,seed):
        VNS.solve(self,seed)

        x = self.gen_initial_solution()
        #print("Initial solution: " + str(x) + " -----> Value: " + str(self.evaluation_function(x)))

        for i in range(3):
            #print("Iteration " + str(i))
            self.k = 0
            while self.k<self.k_max:
                x_new = self.shake(x)
                x = self.neighbourhood_change_sequential(x,x_new)
                #print("     Current solution: " + str(x) + " -----> Value: " + str(self.evaluation_function(x)))
        
        #print("Best solution: " + str(x) + " -----> Value: " + str(self.evaluation_function(x)))
        return x,self.evaluation_function(x)


   
        