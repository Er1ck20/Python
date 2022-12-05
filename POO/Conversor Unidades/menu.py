import os
from Longitud import Longitud
from Volumen import Volumen
from Peso import Peso
menu = None

while menu != 4:

    # Funcion para limpiar
    def cls():
        os.system('cls')

    menu = int(input('1. Conversor de Longitud \n2. Conversor de Volumen \n3. Conversor de Peso \n4. Salir \nSeleccione(1-4): '))

    cls()

    try:
        if menu == 1:
            submenu = None
            while submenu != 9:
                submenu = int(input('1. Convertir Pulgada a Milimetros \n2. Convertir Yarda a Metros \n3. Convertir Milla a Kilometros \n4. Convertir Pulgada^2 a Centimetros \n5. Convertir Pie^2 a Metros^2 \n6. Convertir Yarda^2 a Metros^2 \n7. Convertir Acre a Hectareas \n8. Convertir Milla^2 a Kilometros^2 \n9. Salir \nSeleccione(1-9): '))

                cls()

                try:
                    if submenu == 1:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        l = Longitud(x)
                        l.conversion_pulgada()
                    
                    elif submenu == 2:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        l = Longitud(x)
                        l.conversion_yarda()
                    
                    elif submenu == 3:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        l = Longitud(x)
                        l.conversion_milla()
                    
                    elif submenu == 4:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        l = Longitud(x)
                        l.conversion_pulgada2()
                    
                    elif submenu == 5:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        l = Longitud(x)
                        l.conversion_pie2()
                    
                    elif submenu == 6:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        l = Longitud(x)
                        l.conversion_yarda2()
                    
                    elif submenu == 7:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        l = Longitud(x)
                        l.conversion_acre()
                    
                    elif submenu == 8:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        l = Longitud(x)
                        l.conversion_milla2()
                        
                except Exception as ex:
                    raise {ex}
        
        elif menu ==2:
            submenu = None
            while submenu != 5:
                submenu = int(input('1. Convertir de Pie^3 a Metros^3 \n2. Convertir de Yarda^3 a Metros^3 \n3. Convertir de Pinta a Litros \n4. Convertir de Galon a Litros \n5. Salir \nSeleccione(1-5): '))

                cls()
                try:
                    if submenu == 1:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        v = Volumen(x)
                        v.conversion_pie3()
                    
                    elif submenu == 2:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        v = Volumen(x)
                        v.conversion_yarda3()
                    
                    elif submenu == 3:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        v = Volumen(x)
                        v.conversion_pinta()
                    
                    elif submenu == 4:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        v = Volumen(x)
                        v.conversion_galon()
                    
                except Exception as ex:
                    raise {ex}

        elif menu ==3:
            submenu = None
            while submenu != 4:
                submenu = int(input('1. Convertir de Onza a Gramos \n2. Convertir de Libra a Kilogramos \n3. Convertir de Toneladas Inglesas a Toneladas \n4. Salir \nSeleccione(1-5): '))

                cls()
                try:
                    if submenu == 1:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        p = Peso(x)
                        p.conversion_onza()
                    
                    elif submenu == 2:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        p = Peso(x)
                        p.conversion_libra()
                    
                    elif submenu == 3:
                        x = int(input('Proporcione la medida que desea convertir: '))
                        p = Peso(x)
                        p.conversion_toneladaI()
                    
                except Exception as ex:
                    raise {ex}


    except Exception as ex:
        print(f'ERROR: {ex}')