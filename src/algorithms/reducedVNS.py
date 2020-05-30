from src.algorithms.vns import VNS


class ReducedVNS(VNS):

    def solve(self, seed: int):
        VNS.solve(self, seed)

        x_cur = self.gen_initial_solution()  # Generation of a solution

        for _ in range(3):

            self.k = 1

            while self.k < self.k_max:
                x_new = self.shake(x_cur)  # Shakes the current solution

                x_cur, self.k = self.neighbourhood_change_sequential(x_cur, x_new,
                                                                     self.k)  # Choice of the best solution

        return x_cur, self.evaluation_function(x_cur)
