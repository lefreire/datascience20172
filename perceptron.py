import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, eta, tol):
        self.eta = eta
        self.tol = tol

    def sech(self, x):
        return 1/np.cosh(x)

    def fit(self, X, y):
        X = np.array(X)
        self.w = np.random.random(len(X[0]))
        self.b = np.random.random()
        dif_error = self.tol + 100
        erro_anterior = 1000
        while dif_error > self.tol:
            erro = 0
            b_parcial = 0
            grad = np.zeros(len(self.w))
            for i in xrange(len(X)):
                out = np.dot(self.w, X[i]) + self.b
                parcial = y[i] - np.tanh(out)
                erro += parcial**2
                grad += -2*X[i]*(self.sech(out)**2)*parcial
                b_parcial += -2*(self.sech(out)**2)*parcial
            self.w -= self.eta*grad/len(X)
            self.b -= self.eta*b_parcial/len(X)
            dif_error = abs(erro_anterior - erro)
            erro_anterior = erro
            print erro
        return self.w, self.b

def main():
    percep = Perceptron(0.1, 0.01)
    w, b = percep.fit(([0,2], [-3,4], [2,1]), [-1,1,1])

if __name__ == "__main__":
    main()