class VNS_MUltistart():
    
    def __init__(self,iterations = 1, vns_problem=None):
        self.iterations = iterations
        self.vns_problem = vns_problem
    
    def solve(self):

        aux = [self.vns_problem(seed=i) for i in range(0,self.iterations)]

        return zip(*aux)
