# Dada la sigueinte tupla, crear una lista que solo incluya
# numeros menores que 5.

tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for i in tupla:
    if i < 5:
        lista.append(i)
print(lista)
