# Conversor de divisas

# Importamos el sistema
import os

def Menu():
    menu = None
    
    # Bucle while
    while menu != 6:
        # Manejo de excepciones
        try:
            menu = int(input('1. Dolar \n2. Dolar Canadiense  \n3. Euro  \n4. Libra Esterlina \n5. Peso Dominicano \n6. Salir \nSeleccione: '))

            # Funcion para limpiar la consola.
            def limpiar():
                os.system('cls')
            
            # Llamamos la funcion para limpiar la consola
            limpiar()

            if menu == 1:
                opciones = None
                while opciones != 5:
                    try:
                        opciones = int(input('1. Dolar a Dolar canadiense \n2. Dolar a Euro \n3. Dolar a Libra Esterlina \n4. Dolar a Peso Dominicano \n5. Salir \nSeleccione:'))

                        limpiar()
                        if opciones == 1:
                            dolar = int(input('Proporcione la cantidad: '))
                            DOLAR_CANADIENSE = 1.29406
                            conversion = (dolar * DOLAR_CANADIENSE)
                            print('DOLAR A DOLAR CANADIENSE'.center(50, '-'))
                            print(f'Conversion: {dolar} es igual a: {conversion:.2f} ')
                            
                        
                        elif opciones == 2:
                            dolar = int(input('Proporcione la cantidad: '))
                            EURO = 0.96
                            conversion = (dolar * EURO)
                            print('DOLAR A EURO'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')

                        
                        elif opciones == 3:
                            dolar = int(input('Proporcione la cantidad: '))
                            LIBRA_ESTERLINA = 0.82
                            conversion = (dolar * LIBRA_ESTERLINA)
                            print('DOLAR A LIBRA ESTERLINA'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')

                        elif opciones == 4:
                            dolar = int(input('Proporcione la cantidad: '))
                            PESO_DOM = 55.25
                            conversion = (dolar * PESO_DOM)
                            print('DOLAR A PESO DOMINICANO'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')
                            
                       
                            
                    except Exception as ex:
                        print(f'ERROR: {ex}')
                    
            elif menu == 2:
                opciones = None
                while opciones != 5:
                    try:
                        opciones = int(input('\n1. Dolar Canadiense a Dolar \n2. Dolar Canadiense a Euro \n3. Dolar Canadiense a Libra Esterlia \n4. Dolar Canadiense a Peso Dominicano \n5. Salir \nSeleccione(1-5): '))
                        limpiar()

                        if opciones == 1:
                            Dcanadiense = int(input('Proporcione la cantidad: '))
                            DOLAR = 0.78
                            conversion = (Dcanadiense * DOLAR)
                            print('DOLAR CANADIENSE A DOLAR'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')
                    
                        elif opciones == 2:
                            Dcanadiense = int(input('Proporcione la cantidad: '))
                            EURO = 0.74
                            conversion = (Dcanadiense * EURO)
                            print('DOLAR CANADIENSE A EURO'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')
                    
                        elif opciones == 3:
                            Dcanadiense = int(input('Proporcione la cantidad: '))
                            LIBRA_ESTERLINA = 0.64
                            conversion = (Dcanadiense * LIBRA_ESTERLINA)
                            print('DOLAR CANADIENSE A LIBRA ESTERLINA'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')

                        elif opciones == 4:
                            Dcanadiense = int(input('Proporcione la cantidad: '))
                            PESO_DOM = 43.38
                            conversion = (Dcanadiense * PESO_DOM)
                            print('DOLAR CANADIENSE A PESO DOMINICANO'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')
                    

                    except Exception as ex:
                        print(f'ERROR: {ex}')

            elif menu == 3:
                opciones = None
                while opciones != 5:
                    try:
                        opciones = int(input('\n1. Euro a Dolar\n2. Euro a Dolar Canadiense \n3. Euro a Libra Esterlia \n4. Euro a Peso Dominicano \n5. Salir \nSeleccione(1-5): '))
                        limpiar()
                        if opciones == 1:
                            Euro = int(input('Proporcione la cantidad: '))
                            DOLAR = 1.05
                            conversion = (Euro * DOLAR)
                            print('EURO A EURO'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')

                        elif opciones == 2:
                            Euro = int(input('Proporcione la cantidad: '))
                            DOLAR_CANADIENSE = 1.34
                            conversion = (Euro * DOLAR_CANADIENSE)
                            print('EURO A DOLAR CANADIENSE'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')

                        elif opciones == 3:
                            Euro = int(input('Proporcione la cantidad: '))
                            LIBRA_ESTERLINA = 0.65
                            conversion = (Euro * LIBRA_ESTERLINA)
                            print('EURO A LIBRA ESTERLINA'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')
                        
                        elif opciones == 4:
                            Euro = int(input('Proporcione la cantidad: '))
                            PESO_DOM = 0.65
                            conversion = (Euro * PESO_DOM)
                            print('EURO A PESO DOMINICANO'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')
                        
                       
                            
                    except Exception as ex:
                        print(f'ERROR: {ex}')
            
            elif menu == 4:
                opciones = None
                while opciones != 5:
                    try:
                        opciones = int(input('\n1. Libra Esterlina a Dolar \n2. Libra Esterlina a Dolar Canadiense \n3. Libra Esterlina a Euro \n4. Libra Esterlina a Peso Dominicano \n5. Salir \nSeleccione(1-5): '))
                        limpiar()

                        if opciones == 1:
                            LEsterlina = int(input('Proporcione la cantidad: '))
                            DOLAR = 1.23
                            conversion = (LEsterlina * DOLAR)
                            print('LIBRA ESTERLINA A DOLAR'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')
                        
                        elif opciones == 2:
                            LEsterlina = int(input('Proporcione la cantidad: '))
                            DOLAR_CANADIENSE = 1.57
                            conversion = (LEsterlina * DOLAR_CANADIENSE)
                            print('LIBRA ESTERLINA A DOLAR CANADIENSE'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')

                        elif opciones == 3:
                            LEsterlina = int(input('Proporcione la cantidad: '))
                            EURO = 1.17
                            conversion = (LEsterlina * EURO)
                            print('LIBRA ESTERLINA A EURO'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')
                        
                        elif opciones == 4:
                            LEsterlina = int(input('Proporcione la cantidad: '))
                            PESO_DOM = 68.23
                            conversion = (LEsterlina * PESO_DOM)
                            print('LIBRA ESTERLINA A PESO DOMINICANO'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')
                        
                
                    
                    except Exception as ex:
                        print(f'ERROR: {ex}')


            elif  menu == 5:
                opciones = None
                while opciones != 5:
                    try:
                        opciones = int(input('\n1. Peso Dominicano a Dolar \n2. Peso Dominicano a Dolar Canadiense \n3. Peso Dominicano a Euro \n4. Peso Dominicano a Libra Esterlina \n5. Salir \nSeleccione(1-5): '))
                        limpiar()

                        if opciones == 1:
                            Pdom = int(input('Proporcione la cantidad: '))
                            DOLAR = 0.018
                            conversion = (Pdom * DOLAR)
                            print('PESO DOMINICANO A DOLAR'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')

                        elif opciones == 2:
                            Pdom = int(input('Proporcione la cantidad: '))
                            DOLAR_CANADIENSE = 0.023
                            conversion = (Pdom * DOLAR_CANADIENSE)
                            print('PESO DOMINICANO A DOLAR CANADIENSE'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')

                        elif opciones == 3:
                            Pdom = int(input('Proporcione la cantidad: '))
                            EURO = 0.017
                            conversion = (Pdom * EURO)
                            print('PESO DOMINICANO A EURO'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')
                        
                        elif opciones == 4:
                            Pdom = int(input('Proporcione la cantidad: '))
                            LIBRA_ESTERLINA = 0.015
                            conversion = (Pdom * LIBRA_ESTERLINA)
                            print('PESO DOMINICANO A LIBRA ESTERLINA'.center(50, '-'))
                            print(f'Conversion: {conversion:.2f}')
                        
                        

                    except Exception as ex:
                        print(f'ERROR: {ex}')
               
        
        except Exception as ex:
            print(f'Error: {ex}')

# Llamamos la funcion
Menu()