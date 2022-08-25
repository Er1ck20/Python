# Crea un programa que le pida al usuario que ingresu su nombre y edad.
# Imprima un mensaje dirigido a ellos que le diga el age en que cumpliran 100

nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))

r = (2022 - edad) + 100 
print(f'Hola {nombre}, actualmente tienes {edad} y cumpliras 100 en el age {r}')