# Etapas de la vida
# 0-10: Infancia.
# 10-20: Muchos cambios y mucho estudio.
# 20-30 : Amor y comienza el trabajo.

Edad = int(input('Proporciona tu Edad: '))
if Edad < 10:
    print(f'Tu edad es: {Edad}, La infancia es increible.')
elif 10 <= Edad < 20:
    print(f'Tu edad es: {Edad}, Muchos cambios y mucho estudio.')
elif 20 <= Edad < 30:
    print(f'Tu edad es: {Edad}, Amor y comienza el trabajo.')
else:
    print('Error, Etapa de la vda no reconocida.')
