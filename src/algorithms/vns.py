from functools import reduce
import random
import numpy as np

class VNS():

    def __init__(self,problem):

        self.problem = problem
        self.evaluation_function = self.problem.evaluation_function
        self.N = self.problem.neighbour_structure
        self.k_max = len(self.N)
        self.k =0 # Reset neighbour structure to the first structure

        self.num_evaluations = 0
    
    def gen_initial_solution(self):
        '''
        Generates an initial solution
        '''
        
        #initial_sol = [random.randint(0,1) for i in range(self.problem.num_objects)]
        initial_sol = np.random.randint(2,size=self.problem.num_objects)

        while(self.problem.feasible_solution(initial_sol) == False):
            print("no valid " + str(initial_sol))
            #initial_sol = [random.randint(0,1) for i in range(self.problem.num_objects)]
            initial_sol = np.random.randint(2,size=self.problem.num_objects)
        
        print("initial" + str(initial_sol))
        return initial_sol

    def shake(self,x_cur):
        '''
        Generates randomly a neighbour solution of another solution x_cur given a neighbour structure n
            Args:
                x_cur (str): A problem solution
        '''

        print("shake" + str(x_cur))
        #neighbourhood_structure = self.N[self.k]
        #print("shake3" + str(neighbourhood_structure))
        print("shake4" + str(x_cur))
        #neighbours = neighbourhood_structure(x=x_cur)
        neighbours = self.problem.gen_neighbourhood(x=x_cur,distance=self.k)
        print("neighbours2" + str(neighbours))
        
        #return random.choice(neighbours)

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
        random.seed(seed)
        np.random.seed(0)



   
        