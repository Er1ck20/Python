# Realizar un programa que calcule el numero salario de un empleado al obtener x% de aumento.

salario = float(input('Proporcione su salario: '))

# Funcion para determinar el nuevo salario
def salario_incremento(x):
    aumento = int(input('Introduzca el aumento: '))
    y = (aumento / 100) * x
    r = (x + y)
    return f'Salario actual: {x} y obutvo un aumento del {aumento}%, su nuevo salario es de ${r}'

print(salario_incremento(salario))