# Construye un programa que al recibir tres valores numericos diferentes entre si, determine los mismo en orden creciente

num1 = int(input('Primer numero: '))
num2 = int(input('Segundo numero: '))
num3 = int(input('Tercer numero: '))

if num1 < num2 < num3:
    print(f'El orden es creciente: {num1} {num2} {num3}')
else:
    print(f'El orden no es creciente')
