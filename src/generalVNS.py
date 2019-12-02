from functools import reduce
import random
from vns import VNS

class GeneralVNS(VNS):
    
    def improvement_function(self,x_cur):

        stop = False

        while stop==False:
            l = 0
            x_prime = x_cur

            while l<self.k_max:
                neighbourhood_structure = self.N[l]
                neighbours = list(neighbourhood_structure(x_cur))

                best_sol = max(neighbours,key=self.evaluation_function)
                x_cur,l = self.neighbourhood_change_sequential(x_cur,best_sol,l)

                if self.evaluation_function(x_prime)>=self.evaluation_function(x_cur):
                    stop=True
        return x_prime

    def solve(self):

        x = self.gen_initial_solution()
        print("Initial solution: " + str(x) + " -----> Value: " + str(self.evaluation_function(x)))

        for i in range(3):
            print("Iteration " + str(i))
            self.k = 0
            while self.k<self.k_max:
                x_new = self.shake(x)
                x_local = self.improvement_function(x_new)
                x = self.neighbourhood_change_sequential(x,x_local)
                print("     Current solution: " + str(x) + " -----> Value: " + str(self.evaluation_function(x)))
        
        print("Best solution: " + str(x) + " -----> Value: " + str(self.evaluation_function(x)))
        return x


   
        