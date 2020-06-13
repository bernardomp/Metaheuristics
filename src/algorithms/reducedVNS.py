from typing import Tuple

from algorithms.vns import VNS


class ReducedVNS(VNS):

    def solve(self, seed: int) -> Tuple[list, float]:
        VNS.solve(self, seed)

        # Generation of a solution
        x_cur = self.gen_initial_solution()

        for _ in range(3):

            self.k = 1

            while self.k < self.k_max:
                # Shakes the current solution
                x_new = self.shake(x_cur)

                # Choice of the best solution
                x_cur, self.k = self.neighbourhood_change_sequential(x_cur, x_new, self.k)

        return x_cur, self.evaluation_function(x_cur)
