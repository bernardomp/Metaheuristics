from functools import reduce
import random
import numpy as np

class VNS():

    def __init__(self,problem):

        self.problem = problem
        self.evaluation_function = self.problem.evaluation_function
        

        self.k =0 # Reset neighbour structure to the first structure

        #Defines the maximum number of neighbourhood structures
        if self.problem.num_objects < 5:
            self.k_max=self.problem.num_objects//2 + 1
        else:
            self.k_max = 6

   
    def gen_initial_solution(self):
        '''
        Generates an initial solution
        '''
    
        
        initial_sol = np.random.randint(2,size=self.problem.num_objects)

        while(self.problem.feasible_solution(initial_sol) == False):
            
            initial_sol = np.random.randint(2,size=self.problem.num_objects)
        
        return initial_sol
        

    def shake(self,x_cur):
        '''
        Generates randomly a neighbour solution of another solution x_cur given a neighbour structure n
            Args:
                x_cur (str): A problem solution
        '''
       
        neighbours = self.problem.gen_neighbourhood(x=x_cur,distance=self.k)
        element = np.random.choice(np.arange(len(neighbours)))

        return neighbours[element]

    
    def neighbourhood_change_sequential(self,x_cur,x_new,k):

        x_aux = None

        if self.evaluation_function(x_cur)<self.evaluation_function(x_new):
            x_aux = x_new
            k=0
        else:
            k+=1
            x_aux = x_cur

        return x_aux,k


    def improvement_function(self,x_cur):
        pass

    def solve(self,seed=0):
        np.random.seed(seed)



   
        