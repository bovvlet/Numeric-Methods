import numpy as np

class NumericMethod:
    def __init__(self, x_0, y_0, x_n, N, n_0, n_max):
        self.x_0 = x_0
        self.y_0 = y_0
        self.x_n = x_n
        self.N = N
        self.n_0 = n_0
        self.n_max = n_max
        self.xs = np.array([])
        self.ys = np.array([])
        self.y_error = np.array([])
        self.y_global_error = np.array([])

    '''each method has it's own method'''
    def compute_points(self, H):
        pass

    '''computes error for some fixed N'''
    def compute_errors(self, H):
        self.y_error = np.array([])
        self.compute_points(H)
        x = self.x_0
        h = self.xs[1] - self.xs[0]
        for y in self.ys:
            self.y_error = np.append(self.y_error, np.fabs(self.y_exact(x) - y))
            x += h

    '''computes errors in some range of values for N'''
    def compute_global_errors(self):
        self.y_global_error = np.array([])
        for H in range(self.n_0, self.n_max+1):
            self.compute_points(H)
            self.compute_errors(H)
            self.y_global_error = np.append(self.y_global_error, max(self.get_error_array()))

    '''getters'''
    def get_x_array(self):
        return self.xs

    def get_y_array(self):
        return self.ys

    def get_error_array(self):
        return self.y_error

    def get_global_error(self):
        return self.y_global_error

    '''functions with y' and general solutions'''
    def constant(self):
        return (np.exp(-self.y_0) - self.x_0) / (self.x_0 * self.x_0)

    def y_exact(self, x):
        return -(np.log(self.constant() * x * x + x))

    def y_prime(self, x, y):
        return np.exp(y) - (2 / x)