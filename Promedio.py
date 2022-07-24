# Promedio

print('PROMEDiO'.center(100, '-'))

Leng = int(input('Proporcione la nota de Lenguaje: '))
Mat = int(input('Proporcione la nota de Matematica: '))
Nat = int(input('Proporcione la nota de Naturales: '))
Soc = int(input('Proporcione la nota de Sociales: '))

PROMEDIO = (Leng + Mat + Nat + Soc) // 4

if PROMEDIO >= 90:
    print(f'USTED TIENE UN PROMEDIO DE: {PROMEDIO} y OBTUVO UNA A')

elif PROMEDIO >= 80 < 89:
    print(f'USTED TIENE UN PROMEDIO DE: {PROMEDIO} y OBTUVO UNA B')

elif PROMEDIO >= 74 < 79:
    print(f'USTED TIENE UN PROMEDIO DE: {PROMEDIO} y OBTUVO UNA C')

elif PROMEDIO >= 70 < 74:
    print(f'USTED TIENE UN PROMEDIO DE: {PROMEDIO} y OBTUVO UNA D')

elif PROMEDIO < 70:
    print(f'REPROBRADO!!')

else:
    print('FIN')