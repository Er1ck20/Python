Menu = int(input('OPCIONES: \n1. Celsius a Fahrenheit '
                 '\n2. Fahrenheit a Celsius '
                 '\n3. Salir '
                 '\nSeleccione(1-3): '))

if Menu == 1:
    x = int(input('Proporcione la temperatura: '))
    r = x * 9 / 5 + 32
    print(f'C a F: {r}')

elif Menu == 2:
    x = int(input('Proporcione la temperatura: '))
    r = (x - 32) * 5 / 9
    print(f'F a C: {r:.2f}')
