from Banco import Banco
import os
import getpass

Menu = None

while Menu != 4:

    try:
        def limpiar():
            os.system('cls')

        Menu = int(input('1. Depositar Efectivo \n2. Retirar Efectivo \n3. Ver Total \n4. Salir \nSeleccionar(1-4): '))
        limpiar()
        if Menu == 1:
            nombre = input('Ingrese su nombre: ')
            cedula = int(input('Ingrese su cedula: '))
            password = getpass.getpass('Ingrese su password: ')
            password2 = getpass.getpass('Vuelva a ingresar su password: ')

            try:
                if password == password2:
                    C1 = Banco(nombre, cedula)
                    print(C1)
                    C1.depositar()
                    C1.total()
                else:
                    print(f'Las password no coinciden!')
            
            except Exception as ex:
                print(f'ERROR: {ex}')
            
        
        elif Menu == 2:
            nombre = input('Ingrese su nombre: ')
            cedula = int(input('Ingrese su cedula: '))
            password = getpass.getpass('Ingrese su password: ')
            password2 = getpass.getpass('Vuelva a ingresar su password: ')

            try:
                if password == password2:
                    C1 = Banco(nombre, cedula)
                    print(C1)
                    C1.retirar()
                    C1.total()
                else:
                    print(f'Las password no coinciden!')
            
            except Exception as ex:
                print(f'ERROR: {ex}')
            
        
        elif Menu == 3:
            nombre = input('Ingrese su nombre: ')
            cedula = int(input('Ingrese su cedula: '))
            password = getpass.getpass('Ingrese su password: ')
            password2 = getpass.getpass('Vuelva a ingresar su password: ')

            try:
                if password == password2:
                    C1 = Banco(nombre, cedula)
                    C1.total()
                else:
                    print(f'Las password no coinciden!')
            
            except Exception as ex:
                print(f'ERROR: {ex}')
        
    except Exception as ex:
        print(f'ERROR: {ex}')

else:
    print('FIN')