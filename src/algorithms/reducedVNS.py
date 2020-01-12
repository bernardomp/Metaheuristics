from functools import reduce
import random
from algorithms.vns import VNS

class ReducedVNS(VNS):

    def solve(self,seed):
        VNS.solve(self,seed)

        x_cur = self.gen_initial_solution() #Generation of a solution
       
        for i in range(3):

            self.k = 0

            while self.k<self.k_max:
                print("str: " + str(i) + str(x_cur))
                x_new = self.shake(x_cur) #Shakes the current solution
                print("str1: " + str(self.k))
                x_cur, self.k = self.neighbourhood_change_sequential(x_cur,x_new,self.k) #Choice of the best solution
                print("str2: " + str(self.k))
                print("str3: " + str(x_cur))
        return x_cur, self.evaluation_function(x_cur)


   
        