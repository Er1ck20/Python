import os
import math
# Calculadora

print('CALCULADORA'.center(100, '-'))

Menu = None

while Menu != 6:
    # Funcion para limpiar
    def limpiar():
        os.system('cls')
    try:
        Menu = int(input('\n1. Suma \n2. Resta \n3. Division \n4. Multiplicacion \n5. Potencia \n6. Salir \nSeleccione(1-6): '))
        limpiar()

        if Menu == 1:
            num1 = int(input('Ingrese el primer numero: '))
            num2 = int(input('Ingrese el segundo numero: '))
            r = (num1 + num2)
            print('SUMA'.center(50, '-'))
            print(f'El resultado de la suma es: {r}')
        
        elif Menu == 2:
            num1 = int(input('Ingrese el primer numero: '))
            num2 = int(input('Ingrese el segundo numero: '))
            r = (num1 - num2)
            print('RESTA'.center(50, '-'))
            print(f'El resultado de la resta es: {r}')
        
        elif Menu == 3:
            num1 = int(input('Ingrese el primer numero: '))
            num2 = int(input('Ingrese el segundo numero: '))
            r = (num1 // num2)
            print('DIVISION'.center(50, '-'))
            print(f'El resultado de la division es: {r}')
        
        elif Menu == 4:
            num1 = int(input('Ingrese el primer numero: '))
            num2 = int(input('Ingrese el segundo numero: '))
            r = (num1 * num2)
            print('MULTIPLICACION'.center(50, '-'))
            print(f'El resultado de la multiplicacion es: {r}')
        
        elif Menu == 5:
            num1 = int(input('Ingrese el primer numero: '))
            num2 = int(input('Ingrese el segundo numero: '))
            r = math.pow(num1, num2)
            print('POTENCIA'.center(50, '-'))
            print(f'El resultado de la POTENCIA es: {r}')


    except Exception as ex:
        print(f'ERROR: {ex}')

else:
    print('FIN DEL PROGRAMA.')
