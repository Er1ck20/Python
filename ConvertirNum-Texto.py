# Convertir Numeros enteros a Texto.

numero = int(input('Escribe un valor entre 1 y 3: '))

if numero == 1:
    numeroTexto = 'Uno'
elif numero == 2:
    numeroTexto = 'Dos'
elif numero == 3:
    numeroTexto = 'Tres'
else:
    numeroTexto = 'Fuera de Rango'

print(f'Numero seleccionado: {numero} = {numeroTexto}')
