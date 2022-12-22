# Realizar un programa que pida dos numeros al usuario y una operacion matematica se ejecute con esos dos numeros:

x = float(input('Primer numero: '))
y = float(input('Segundo numero: '))
# Funcion donde haremos las operaciones
def operaciones(x, y):

# Usaremos funciones anidadas - Funciones dentro de las funciones.

    # Funcion para sumar
    def suma(x, y):
        r = (x + y)
        return f'El resultado de la suma es: {r}'
    
    # Funcion para restar
    def resta(x,y):
        r = (x - y)
        return f'El resultado de la resta es: {r}'

    # Funcion para multiplicar
    def mutiplicacion(x,y):
        r = (x * y)
        return f'El resultado de la multiplicacion es: {r}'

    # Funcion para dividir
    def division(x,y):
        r = (x / y)
        return f'El resultado de la division es: {r}'
    
    # Funcion para sacar el exponente
    def exponiente(x,y):
        r = (x ** y)
        return f'El resultado de la exponienciacion es: {r:.0f}'

    # Retornamos
    return f'''
    {suma(x,y)}
    {resta(x,y)}
    {mutiplicacion(x,y)}
    {division(x,y)}
    {exponiente(x,y)}
    '''


print(operaciones(x,y))