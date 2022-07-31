# Crear un codigo que obtenga el promedio de un set(conjunto) de numeros dados por el usuario.

# Variable para pedirle al usuario el tama;o del conjunto de numeros.
# Hacer un loop(Bucle) para pedirle cada numero del set(conjunto).
# Hacer el calculo.
# IMPRIMIR EL RESULTADO.

conjunto = int(input('Proporcione el tama;o del conjunto de numeros: '))
# Le asignamos el valor de 0 a la variable x
x = 0
# Bucle for donde obtendremos el rango de i que sera dado por el conjunto de numeros que proporcionara el usuario final.
for i in range(conjunto):

    # Introducciones los numeros que estaran en el conjunto de numeros
    numeros = int(input('Numeros del conjunto: '))
    # Almacenamos la suma de los numeros del conjunto en la variable x
    x = x + numeros
    
resultado = x / numeros
# Imprimimos el promedio.
print(f'El promedio es: {resultado}')

