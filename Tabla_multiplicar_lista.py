# Pide un numero por teclado y guarda en una lista su tabla de multiplicar.

num = int(input('Proporcione un numero: '))

lista = []

for i in range(1, 13):
    r = num * i
    lista.append(r)

print(f'{lista}')