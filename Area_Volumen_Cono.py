# Importamos el modulo de math
import math

# Calcular el area y el volumen de un CONO.

# Datos
# El areabase se calcula: AB = pi * radio ^ 2
# El area lateral se calcula: AL = pi * radio * generatriz
# El area total se calcula: AT = AB + AL
# El volumen se calcula: V = (1/3) * AB * ALTURA

RADIO = int(input('Proporcione el radio: '))
ALTURA = int(input('Proporcione la altura: '))
# Generatriz
GENE = int(input('Proporcione la generatriz: '))

# Area de la base
AB = math.pi * (RADIO ** 2)
print(f'El area de la base es igual a: {AB:.2f}')

# Area lateral
AL = math.pi * RADIO * GENE
print(f'El area lateral es igual a: {AL:.2f}')

# Area Total
AT = AB + AL
print(f'EL area total es igual a: {AT:.2f}')

# Volumen
V = (1/3) * AB * ALTURA
print(f'El volumen es igual a: {V:.2f}')
