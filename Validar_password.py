# Realizar un programa que valide si una password es segura.
# Debe tener mas de 8 caracteres.
# Debe tener almenos una letra mayuscula.
# Debe tener almenos un numero.

# Importamos getpass - Nos ayudara a ocultar la password
import getpass

# Funcion para validar la password
def validar_password(password):
    # El largo de nuestra password debe ser igual o mayor a 9
    if len(password) >= 8:
        # Bucle for que recorrera el rango de nuestra password
        for i in range(len(password)):
            # Preguntamos si en la password hay alguna letra en mayuscula o algun numero
            if password[i].isupper() and password[i].isnumeric():
                # Si es el caso devolvera true
                return True
        print(f'La password es segura')
    else:
        print('La password es insegura.')

p = getpass.getpass('Ingrese su password: ')
p2 = getpass.getpass('Vuelva a ingresar su password: ')
# Validamos que la password sea igual
if p == p2:
    # Lllamamos la funcion
    validar_password(p)
else:
    print(f'Las password no coinciden')


