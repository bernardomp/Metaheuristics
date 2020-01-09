from functools import reduce
import random
from algorithms.vns import VNS

class BasicVNS(VNS):
    
    def improvement_function(self,x_cur):

        neighbourhood_structure = self.N[self.k]
        neighbours = list(neighbourhood_structure(x_cur))

        return max(neighbours,key=self.evaluation_function)


    def solve(self,seed):
        VNS.solve(seed)

        x_cur = self.gen_initial_solution()

        for i in range(3):
            
            self.k = 0

            while self.k<self.k_max:
                x_new = self.shake(x_cur)
                x_local = self.improvement_function(x_new)
                x_cur, self.k = self.neighbourhood_change_sequential(x_cur,x_local,self.k)
        
        return x_cur, self.evaluation_function(x_cur)


   
        