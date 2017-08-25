import numpy as np

def grad(x):
    return np.array([2*x[0], 2*x[1]])

# given a point, find the local minimum of the function x^2 + y^2 using grad
def graddescent(x0, eta=0.1, tol=0.01):
    x = x0[:]
    diff = 100
    while diff > tol:
        xant = x[:]
        x = x - eta*grad(x)
        diff = np.linalg.norm(x - xant)
    return x

print graddescent([4,4])