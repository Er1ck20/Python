# Realizar una funcion que indique si un numero es par o impar.

def p(x):
    if x %2 == 0:
        return f'{x} es un numero par.'
    else:
        return f'{x} es un numero impar.'

x = int(input('Numero: '))
print(p(x))
