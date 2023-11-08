import matplotlib.pyplot as plt
import numpy as np
import math

class MY_LINE:
    A = 0
    k = 0
    x = 0
    y = 0
    n = 100

    def __init__(self):
        self.A = float(input("Input value of A: "))
        self.k = float(input("Input value of k: "))
    
    def generate(self):
        self.n = 100
        self.x = np.linspace(0, self.A, self.n)
        self.y = self.x ** (3 / 2) / (3 * math.sqrt(self.A)) - math.sqrt(self.A) * (self.x ** (1 / 2)) + 2 * self.A / 3
        plt.plot(self.x, self.y)
        plt.grid(True)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('$f(x)=x ^ 1.5 / (3 * math.sqrt(A)) - math.sqrt(A) * (x ^ 0.5) + 2 * A / 3$')
        plt.show()

my_line = MY_LINE()
my_line.generate()