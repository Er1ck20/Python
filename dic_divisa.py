# Escribir un programa que guarda en una variable el diccionario {'Euro': '€', 'Dolar': '$', 'Yen': '¥'}, pregunte al usuario por una divisa y muestre su simbolo, y muestra un mensaje si la divisa no esta en el dic.

dic_divisa = {'Euro': '€','Dolar': '$','Yen': '¥'}

# Ejercicio 1
x = input('Que divisa desea ver? ')

if x == 'Dolar':
    print(f'{x} - {dic_divisa["Dolar"]}')

elif x == 'Euro':
    print(f'{x} - {dic_divisa["Euro"]}')

elif x == 'Yen':
    print(f'{x} - {dic_divisa["Yen"]}')

else:
    print(f'No se encontro la divisa')


# Ejercicio #2
# Otra forma de hacerlo.
y = input('Que divisa desea ver? ')
# title() - Devolvera la primera palabra de cada oracion en mayuscula.
y = y.title()

if y in dic_divisa:
    print(f'{y} - {dic_divisa[y]}')
else:
    print(f'No se encontro la divisa')