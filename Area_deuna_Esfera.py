# Importamos
import math

# Datos
# El area de una esfera se calcula: Area = 4 * pi * radio ^ 2
# El volumen de una esfera se calcula: V = 1/3 * pi * radio ^ 3

RADIO = float(input('Proporcione el radio: '))

A = 4 * math.pi * (RADIO ** 2)
print(f'El area de una esfera es igual a: {A:.2f}')

V = 1/3 * math.pi * (RADIO ** 3)
print(f'El volumen de una esfera es igual a: {V:.2f}')