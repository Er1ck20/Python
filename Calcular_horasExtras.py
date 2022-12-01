# Realizar un programa donde podamos calcular las horas extras trabajadas, dependiendo la turno. El maximo de horas extras permitidas es de 30.

# Turno #1 - Se pagan a 116 
# Turno #2 -  Se pagan a 135
# Turno #3 - Se pagan a 150

menu = None

while menu != 4:
    menu = int(input('1. Turno #1 \n2. Turno #2 \n3. Turno #3 \n4. Salir \nSeleccionar(1-4): '))

    try:
    
        if menu == 1:
            print(f'HORAS EXTRAS'.center(50, '-'))
            horas = int(input('Horas trabajadas: ')) 
            if horas > 30:
                print(f'Usted se ha excedido de horas extras permitidas, solo se le pagaran 30 que es el maximo estimado.')
                horas = 30
                PAGO = 116
                r = (horas * PAGO)
                print(f'Usted tiene un total de {r} pesos en horas extras.')
            else:
                PAGO = 116
                r = (horas * PAGO)
                print(f'Usted tiene un total de {r} pesos en horas extras.')
        
        elif menu == 2:
            print(f'HORAS EXTRAS'.center(50, '-'))
            horas = int(input('Horas trabajadas: ')) 
            if horas > 30:
                print(f'Usted se ha excedido del maximo de horas extras permitidas, solo se le pagaran 30 que es el maximo estimado.')
                horas = 30
                PAGO = 135
                r = (horas * PAGO)
                print(f'Usted tiene un total de {r} pesos en horas extras.')
            else:
                PAGO = 135
                r = (horas * PAGO)
                print(f'Usted tiene un total de {r} pesos en horas extras.')
        
        elif menu == 3:
            print(f'HORAS EXTRAS'.center(50, '-'))
            horas = int(input('Horas trabajadas: ')) 
            if horas > 30:
                print(f'Usted se ha excedido de horas extras permitidas, solo se le pagaran 30 que es el maximo estimado.')
                horas = 30
                PAGO = 150
                r = (horas * PAGO)
                print(f'Usted tiene un total de {r} pesos en horas extras.')
            else:
                PAGO = 150
                r = (horas * PAGO)
                print(f'Usted tiene un total de {r} pesos en horas extras.')
    
    except Exception as ex:
        print(f'ERROR: {ex}')