import psycopg2 as db

Conexion = db.connect(user='postgres', password='admin20', host='127.0.0.1', port='5432', database='Escuela')

try:
    with Conexion as CON:
        with Conexion.cursor() as CURSOR:
            sentencia = 'INSERT INTO ESTUDIANTES(nombre, apellido, email, edad) VALUES (%s, %s, %s, %s)'
            valores = ('Erick', 'P', 'Prueba@prueba.com', 23)
            CURSOR.execute(sentencia, valores)
            registro = CURSOR.rowcount
            print(f'Estudiante Registrado: {registro}')
except Exception as ex:
    print(f'Error: {ex}')

finally:
    Conexion.close()