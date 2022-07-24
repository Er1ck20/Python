
cadena = 'Hola Mi buen amigo vamos a invertir esto'

print(cadena[::-1])

print('\n')
# Otra forma de hacerlo mediante una funcion/

# Definimos la funcion
def invertir_cadena(cadena):
    # Creamos una variable vacia
    cadena_invertirda = ''
    # Bucle for 
    for i in cadena:
        # Le damos el valor de i a la variable cadena_invertirda
        cadena_invertirda = i + cadena_invertirda
    
    # Retornamos
    return cadena_invertirda

# Llamamos la funcion y le asignamos un valor.
print(invertir_cadena('Aprendiendo'))