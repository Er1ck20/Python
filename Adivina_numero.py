# Adivina el numero del 1 al 10
import random

numero = random.choice(range(1, 10, 1))
adivina = int(input('Proporcione un numero del 1 al 10: '))

if (numero == adivina):
    print('Haz Ganado')

elif (numero != adivina):
    print('Haz Perdido')

else:
    raise ValueError('Introduzca un numero del al 10 ') 


