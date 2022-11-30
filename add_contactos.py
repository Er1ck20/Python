# Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas.



menu = None
# Bucle while
while menu != 2:

    menu = int(input('1.Agregar contacto \n2.Salir \nSeleccionar(1-2): '))
    if menu == 1:
        nombre = input('Proporcione el nombre: ')
        telefono = input('Proporcione el numero de telefono: ')
        diccionario = {nombre: telefono}
        print(diccionario)
        
    else:
        print(f'FIN!!')
    
