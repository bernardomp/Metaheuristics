from src.algorithms.vns import VNS


class BasicVNS(VNS):

    def improvement_function(self, x_cur):

        neighbours = self.problem.gen_neighbourhood(x=x_cur, distance=self.k)

        return max(neighbours, key=self.evaluation_function)

    def solve(self, seed: int):
        VNS.solve(seed)

        x_cur = self.gen_initial_solution()

        for _ in range(3):

            self.k = 1

            while self.k < self.k_max:
                x_new = self.shake(x_cur)
                x_local = self.improvement_function(x_new)
                x_cur, self.k = self.neighbourhood_change_sequential(x_cur, x_local, self.k)

        return x_cur, self.evaluation_function(x_cur)
