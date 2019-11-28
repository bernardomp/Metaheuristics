from functools import partial, reduce

class Knapsack:

    def __init__(self):
        self.num_objects = None
        self.capacity = None
        self.values = []
        self. weights = []

    def read_values(self,filename):
        file = open(filename,"r")
        lines = file.readlines()

        aux = list(map(int,lines[0].split(" ")))
       
        self.num_objects = aux[0]
        self.capacity = aux[1]

        self.values = list(map(int,lines[1].split(" ")))
        self.weights = list(map(int,lines[2].split(" ")))

    
    def gen_neighbour_structure(self):
        self.neighbourhood_structure = [ partial(self.hamming_distance,distance=i) for i in range(1,self.num_objects//2 + 1)]
    
    def __str__(self):
        return "Capacity: " + str(self.capacity) + "\n" + \
        "Objects: " + str(self.num_objects) + "\n" + \
        "Values: " + str(self.values) + "\n" + \
        "Weights: " + str(self.weights)

    def evaluation_function(self,x):

        value = 0
        solution = int(x,2)

        for i in range(self.num_objects):

            value+=(solution & (1<<i)) * self.values[i]

        return value

    def feasible_solution(self,x):

        weight = 0
        solution = int(x,2)

        for i in range(self.num_objects):

            weight+=(solution & (1<<i)) * self.weights[i]

            if weight>self.capacity:
                return False

        return True

    def hamming_distance(self,x=None,distance=1):
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
    
        neighbours = []
        char = None

        for i in range(self.num_objects):

            if x[i] == '0':
                char='1'
            else:
                char='0'
        
            neighbours.append(x[:i] + char + x[i+1:])
    
        return neighbours

