import numpy as np

from Methods.NumericMethod import NumericMethod

'''inherits class NumericMethod'''
class RungeKutta(NumericMethod):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    def compute_points(self, H):
        self.xs = np.linspace(self.x_0, self.x_n, H)
        self.ys = np.array([self.y_0])
        h = self.xs[1] - self.xs[0]
        for x in self.xs[0:-1]:
            k_1_i = self.y_prime(x, self.ys[-1])
            k_2_i = self.y_prime(x + h / 2, self.ys[-1] + h / 2 * k_1_i)
            k_3_i = self.y_prime(x + h / 2, self.ys[-1] + h / 2 * k_2_i)
            k_4_i = self.y_prime(x + h, self.ys[-1] + h * k_3_i)
            self.ys = np.append(self.ys, self.ys[-1] + (h / 6) * (k_1_i + 2 * k_2_i + 2 * k_3_i + k_4_i))
    name = 'Runge'





