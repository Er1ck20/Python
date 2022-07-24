# Reemplazar el texto con un emoji
Menu = None

while Menu != 2:
    Menu = int(input('\n1. Reemplazar texto con Emoji \n2. Salir \nSelecccione(1-2): '))

    if Menu == 1:
        text = input('>')
        # Replace = Reemplazar
        text = text.replace( ':|' , '😀')
        text = text.replace('lol', '😂')
        text = text.replace('xd', '🤣')
        text = text.replace('love', '😍')
        print(text)
    

else:
    print('FIN')




