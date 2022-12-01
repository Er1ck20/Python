# Escribir una clase en python que calcule pow(x, n)
# x = es la base
# n = es el exponente

from math import pow

class Pow:
    def __init__(self, x, n):
        self.x = x
        self.n = n
    
    # Metodo para calcular el pow
    def calcular(self):
        r = pow(self.x, self.n)
        print(r)

p = Pow(2, -3)
p.calcular()
