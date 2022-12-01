# Crear un programa que al recibir como dato el salario de un profesor de una universidad, calcule el incremento del salario de acuerdo al siguiente criterio.

# Salario < 21000 - Incrementara un 12%
# Salario > 21000 y salario < 30000 - Incrementara un 8%
# Salario > 30000 y Salario <50000 - Incrementara un 7%
# Salario > 50000 - Incrementara un 6%

salario = int(input('Proporcione su salario: '))

if salario <= 21000:
    aumento = salario * 0.12
    r = salario + aumento
    print(f'El salario actual es de: {r}')
elif salario > 21000 and salario <= 30000:
    aumento = salario * 0.08
    r = salario + aumento
    print(f'El salario actual es de: {r}')
elif salario > 30000 and salario <= 50000:
    aumento = salario * 0.07
    r = salario + aumento
    print(f'El salario actual es de: {r}')
elif salario > 50000:
    aumento = salario * 0.06
    r = salario + aumento
    print(f'El salario actual es de: {r}')