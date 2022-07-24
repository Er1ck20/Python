# Calculadora de IMC

# Formula: peso / estatura^2

peso = int(input('Ingrese su peso en kg: '))

altura = float(input('Ingre su altura en cm: '))

IMC = peso / (altura * altura)

if IMC > 18.5 and IMC < 24.9:
    print(f'Usted tiene un IMC: {IMC:.2f} tiene BAJO PESO')

elif IMC > 25 and IMC < 29.9:
    print(f'Usted tiene un IMC de: {IMC:.2f} tiene SOBREPESO')

elif IMC > 30:
    print(f'Usted tiene un IMC de: {IMC:.2f} tiene OBESIDAD')

else:
    print('FIN')

