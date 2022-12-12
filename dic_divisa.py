# Escribir un programa que guarda en una variable el diccionario {'Euro': '€', 'Dolar': '$', 'Yen': '¥'}, pregunte al usuario por una divisa y muestre su simbolo, y muestra un mensaje si la divisa no esta en el dic.

dic = {'Euro': '€',
'Dolar': '$',
'Yen': '¥'}

divisa = input('Que divisa desea ver? ')

if divisa == 'Dolar':
    print(f'{divisa} - {dic["Dolar"]}')

elif divisa == 'Euro':
    print(f'{divisa} - {dic["Euro"]}')

elif divisa == 'Yen':
    print(f'{divisa} - {dic["Yen"]}')

else:
    print(f'No proporciono ninguna divisa')


# Otra forma de hacerlo.

divisa2 = input('Que divisa desea ver? ')
# title() - Devolvera la primera palabra de cada oracion en mayuscula.
divisa2 = divisa2.title()
print(dic[divisa2])