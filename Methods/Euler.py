import numpy as np

from Methods.NumericMethod import NumericMethod

'''inherits class NumericMethod'''
class Euler(NumericMethod):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    def compute_points(self, H):
        self.xs = np.linspace(self.x_0, self.x_n, H)
        self.ys = np.array([self.y_exact(self.x_0)])
        h = self.xs[1] - self.xs[0]
        for x in self.xs[0:-1]:
            k_1_i = self.y_prime(x, self.ys[-1])
            self.ys = np.append(self.ys, self.ys[-1] + (h * k_1_i))
    name = 'Euler'





