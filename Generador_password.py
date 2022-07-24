import random
print('Generador de Password'.center(50, '-'))

all = 'asdfghjklqwertyuiopzxcvbnm,./;1234567890\|'

cantidad = int(input('Ingrese la cantidad: '))
longitud = int(input('Ingrese la longitud: '))

print('Password Generadas'.center(50, '-'))
# Bucle for - Creamos un range para la cantidad de password que ingresaremos
for i in range(cantidad):
    # Creamos una variable vacia para posteriomente almacenar el random.choice
    p = ''
    # Bucle for - Creamos un range de la longitud de las password
    for x in range(longitud):
        p += random.choice(all)
        
    print(p)