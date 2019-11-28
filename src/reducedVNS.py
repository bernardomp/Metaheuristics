from functools import reduce
import random
import vns

class ReducedVNS(vns.VNS):

    def __init__(self,problem):

        self.problem = problem
        self.evaluation_function = self.problem.evaluation_function
        self.N = self.problem.neighbourhood_structure

        self.k_max = len(self.N)
        self.k = 1

        self.x = "000000"
        self.x_prime=None

    def shake(self):
        
        neighbourhood_structure = self.N[self.k]
        neighbours = list(neighbourhood_structure(x=self.x))

        return random.choice(neighbourhood_structure)

    
    def neighbourhood_change_sequential(self):

        if self.evaluation_function(self.x)<self.evaluation_function(self.x_prime):
            self.x = self.x_prime 
            self.k=1
        else:
            self.k+=1

    def solve(self):

        for i in range(1):
            self.k = 1
            while self.k<self.k_max:
                shake()
                neighbourhood_change_sequential()


   
        