import numpy as np
from tqdm import tqdm

class SNE():
    
    def __init__(self, X, sigma_squared=1):
        self.X = X
        self.sigma_squared = sigma_squared
    
#     def get_p_ji(self, j, i):
#         p_ji = np.exp(-np.sum((X[i] - X[j]) ** 2)/2 * self.sigma_squared)

#         _sum = 0
#         for k in range(len(X)):
#             if k != i:
#                 _sum += np.exp(-np.sum((X[i] - X[k]) ** 2)/2 * self.sigma_squared)

#         return p_ji / _sum
    
#     def get_p(self):
#         p = np.zeros((len(self.X), len(self.X)))
#         for i in range(len(self.X)):
#             for j in range(len(self.X)):
#                 p[j, i] = self.get_p_ji(j, i)
                
#         return p
        
    def get_p(self):
        for _ in tqdm(range(1)):
            p = np.zeros((len(self.X), len(self.X)))
            for j in range(len(self.X)):
                for i in range(len(self.X)):
                    p[j, i] = np.exp(-np.sum((X[i] - X[j]) ** 2)/2 * self.sigma_squared)

            sum_vector = np.zeros(150)
            for i in range(len(self.X)):
                _sum = 0
                for k in range(len(self.X)):
                    if k != i:
                        _sum += np.exp(-np.sum((X[i] - X[k]) ** 2)/2 * self.sigma_squared)
                sum_vector[i] = _sum

            pl = p / sum_vector
            np.fill_diagonal(pl, 0)

            for i in range(len(self.X)):
                for j in range(len(self.X)):
                    pl[i, j] = (pl[i, j] + pl[j, i]) / (2 * len(self.X))
                    pl[j, i] = pl[i, j]
        return pl
        
    def get_q(self):
        pass
    
    def perp(self):
        pass
    
    def get_sigma(self):
        pass
    
    def binary_search(self):
        pass
    
    def main(self):
        pass
    
    def gradient_descent(self):
        pass
