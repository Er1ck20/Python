# Realizar una funcion que devuelva una tabla de multiplicar.

# Funcion tabla de multiplicar y agregamos un parametro x
def tabla_multiplicar(x):
    # Bucle for con un rango del 1 al 13. OJO: EL ultimo numero se emite(el 13)
    for i in range(1, 13):
        r = x * i
        print(f'{x} * {i} = {r}') 

x = int(input('Proporcione el numero: '))
# Llamamos la funcion
tabla_multiplicar(x)