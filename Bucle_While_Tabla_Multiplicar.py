'''
Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero

'''

x = int(input('Proporcione el numero a multiplicar: '))
i = 0
y = 0
while i <= 12:
    y = x * i
    print(f'TABLA DE MULTIPLICACION: {x} * {i} = {y}')
    i += 1

else:
    print('FIN DEL PROGRAMA')
