# Convertir dias en segundos

DIA = int(input('Proporcione los dias que desea convertir en segundos: '))
# 1 Dia tiene 24 horas.
D = DIA * 24
# 1 Minuto tiene 60 segundos.
SEGUNDOS = 60
# 1 Hora tiene 60 minutos.
HORAS = 60

CONVERSION = (D * SEGUNDOS * HORAS)
print(f'{DIA} dia convertidos a segundos es igual a: {CONVERSION} segundos.')