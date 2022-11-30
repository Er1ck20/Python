# Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.

num = int(input('Proporcione un numero: '))
# Lista vacia
lista = []

while num != 0:
    num = int(input('Proporcione un numero: '))
    lista.append(num)

else:
    print('fin')

# sort() - Sirve para ordenar la lista
lista.sort()
print(lista)

# sort(reverse=True), nos ayuda a ordenar los numeros de mayor a menor.
# lista.sort(reverse=True)
# print(lista)
