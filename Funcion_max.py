# Definir una funcion max() que tome como arg dos numerso y  devuelva el mayor de ellos.

def max(a, b):
    if a > b:
        return f'{a} es mayor que {b}'
    else:
        return f'{b} es mayor que {a}'

# Llamamos la funcion
a = int(input('Ingrese el primer numero: '))
b = int(input('Ingrese el segundo numero: '))
print(max(a, b))