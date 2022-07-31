x = int(input('Ingrese un numero: '))

i = 0

print(f'TABLA DE MULTIPLICACION DEL {x}'.center(50, '*'))
# Bucle for - Le agregamos un range que inicia en 1 y termina en 13, OJO el 13 no se muestra termina en 12
for i in range(1, 13):
    r = x * i
    print(f'{x} x {i} = {r}')
    i += 1