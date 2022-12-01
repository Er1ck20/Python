# Realiza un programa que te permita convertir unidades.
# Pulgadas a milemetros - 1 pulgada equivale a 25.40 milimetros.
# Yarda a metros - 1 yarda equivale a 0.9144 metros.
# Milla a kilometros - 1 Milla equivale a 1.6093 kilometros.


menu = None

while menu != 4:
    menu = int(input('1. Convertir de pulgadas a milimetros \n2. Convertir de yardas a metros \n3. Convertir de millas a kilometros \n4. Salir \nSeleccionar(1-4):'))
    try:
        if menu == 1:
            print(f'CONVERSION - PULGADAS A MILIMETROS'.center(50, '*'))
            x = float(input('Pulgadas: '))
            MILIMETROS = 25.40
            conversion = (x * MILIMETROS)
            print(f'El resultado es: {conversion:.2f} Milimetros.')

        elif menu == 2:
            print(f'CONVERSION - YARDAS A METROS'.center(50, '*'))
            x = float(input('Yardas: '))
            METROS = 0.9144 
            conversion = (x * METROS)
            print(f'El resultado es: {conversion:.2f} Metros.')
        
        elif menu == 3:
            print(f'CONVERSION - MILLAS A KILOMETROS'.center(50, '*'))
            x = float(input('Millas: '))
            KILOMETROS = 1.6093
            conversion = (x * KILOMETROS)
            print(f'El resultado es: {conversion:.2f} Kilometros.')

    except Exception as ex:
        print(f'ERROR: {ex}')
else:
    print(f'FIN DEL PROGRAMA.')