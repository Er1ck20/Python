# Crea un programa que toma tres notas de un estudiante y diga la nota final.
# Tenga en cuenta que la primera y segunda nota valen el 30% de la nota final y la tercera el 40%

n1 = float(input('Proporcione la primera nota: '))
n2 = float(input('Proporcione la segunda nota: '))
n3 = float(input('Proporcione la tercera nota: '))

# Funcion para determinar la nota final
def nota_final(nota1, nota2, nota3):
    # n1 y n2 equivalen al 30% (0.3) de la nota final.
    # n3 equivale al 40% (0.4) de la nota final.
    n_final = (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.4)
    # Retornamos la nota final y utilizamos :.2f para mostrar solo dos decimales.
    return f'Nota final: {n_final:.2f}'

# Llamamos la funcion y la imprimimos.
print(nota_final(n1, n2, n3))