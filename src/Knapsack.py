from functools import partial, reduce


class Knapsack:
    '''
    Defines a class for the Knapsack problem
        Args:
            num_objects (int): The amount of objects stated in the problem
            capacity (int): The knapsack capacity
            values (array): An array storing the value of each object
            weights (array): An array storing the weight of each object
    '''
    def __init__(self,num_objects=None,capacity=None,values=[],weights=[]):
        self.num_objects = num_objects
        self.capacity = capacity
        self.values = values
        self. weights = weights

    def read_values(self,filename):
        '''
         Args:
            distance (int): The amount of distance traveled
            destination (bool): Should the fuels refilled to cover the distance?

        Raises:
            RuntimeError: Out of fuel

        Returns:
            cars: A car mileage
        '''
        file = open(filename,"r")
        lines = file.readlines()

        aux = list(map(int,lines[0].split(" ")))
       
        self.num_objects = aux[0]
        self.capacity = aux[1]

        self.values = list(map(int,lines[1].split(" ")))
        self.weights = list(map(int,lines[2].split(" ")))

    def gen_neighbourhood(self,x=None,distance=1):
        potencial_neighbours = self.hamming_distance(x,distance)
        potencial_neighbours = list(filter(self.feasible_solution,potencial_neighbours))

        return potencial_neighbours
    
    def gen_neighbour_structures(self):
        self.neighbour_structure = [ partial(self.gen_neighbourhood,distance=i) for i in range(1,self.num_objects//2+1)]
    
    def __str__(self):
        return "Capacity: " + str(self.capacity) + "\n" + \
        "Objects: " + str(self.num_objects) + "\n" + \
        "Values: " + str(self.values) + "\n" + \
        "Weights: " + str(self.weights)

    def evaluation_function(self,x):
        '''
        Computes the fitness or value of a given solution x
        Args:
            x (str): The binary string to be checked
        '''
        value = 0
        solution = int(x,2)

        for i in range(self.num_objects):
            
            value+=((solution>>i) & 1) * self.values[self.num_objects-i-1]

        return value

    def feasible_solution(self,x):
        '''
        Checks if the solution x fulfill the problem constraints
        Args:
            x (str): The binary string to be checked
        '''
        weight = 0
        solution = int(x,2)

        for i in range(self.num_objects):

            weight+=((solution>>i) & 1) * self.weights[self.num_objects-i-1]

            if weight>self.capacity:
                return False

        return True


    def hamming_distance(self,x=None,distance=1):
        '''
        Given a solution x (represented as a binary string) generates other solutions x1, x2, ..., xn whose
        hamming distance respect to x is within the interval [1,distance].
            Args:
                x (str): A solution of the problem
                distance (int): The maximum hamming distance of the solutions respect to the 
                                original solution.
            Returns
                An array of solutions with hamming distance [1,distance] respect to x.
        '''
        neighbours = set()

        level = self.hamming_distance_one(x)
        neighbours.update(level)

        while(distance>1):
            level = list(map(self.hamming_distance_one,level))
            level = reduce(lambda x,y: x+y, level)

            neighbours.update(level)
            distance-=1
    
        neighbours.discard(x)

        return neighbours

    def hamming_distance_one(self,x):
        '''
        Given a solution x (represented as a binary string) generates other solutions x1, x2, ..., xn whose
        hamming distance respect to x is 1.
            Args:
                x (str): A solution of the problem
            Returns
                An array of solutions with hamming distance 1 respect to x
        '''
    
        neighbours = []
        char = None

        for i in range(self.num_objects):

            if x[i] == '0':
                char='1'
            else:
                char='0'
        
            neighbours.append(x[:i] + char + x[i+1:])
    
        return neighbours

