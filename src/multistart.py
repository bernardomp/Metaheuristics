class VnsMultistart:
    """
    This provides provides a method to execute several runs of an algorithm
    """

    def __init__(self, iterations: int = 1, vns_problem: object = None):
        self.iterations = iterations
        self.vns_problem = vns_problem

    def solve(self):
        solutions = []
        values = []

        for i in range(0, self.iterations):
            sol, value = self.vns_problem.solve(seed=i)

            solutions.append(sol)
            values.append(value)

        return [solutions, values]
