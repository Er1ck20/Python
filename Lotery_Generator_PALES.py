import random

number = '1345678902'

CANTIDAD = 3
LONGITUD = 2

for i in range(CANTIDAD):
    lotery = '' 
    for x in range(LONGITUD):
        lotery += random.choice(number)

    print(lotery)