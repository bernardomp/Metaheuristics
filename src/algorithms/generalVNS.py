from algorithms.vns import VNS


class GeneralVNS(VNS):

    def improvement_function(self, x_cur):

        stop = False

        while not stop:
            level = 1
            x_aux = x_cur

            while level < self.k_max:

                neighbours = self.problem.gen_neighbourhood(x=x_cur, distance=level)

                x_best = max(neighbours, key=self.evaluation_function)
                x_cur, level = self.neighbourhood_change_sequential(x_cur, x_best, level)

                if self.evaluation_function(x_aux) >= self.evaluation_function(x_cur):
                    stop = True

        return x_aux

    def solve(self, seed: int):
        VNS.solve(self, seed)

        x_cur = self.gen_initial_solution()

        for _ in range(3):

            self.k = 1

            while self.k < self.k_max:
                x_new = self.shake(x_cur)
                x_local = self.improvement_function(x_new)
                x_cur, self.k = self.neighbourhood_change_sequential(x_cur, x_local, self.k)

        return x_cur, self.evaluation_function(x_cur)
