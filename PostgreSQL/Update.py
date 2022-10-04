import psycopg2 as db

Conexion = db.connect(user='postgres', password='admin20', host='127.0.0.1', port='5432', database='Escuela')

try:
    with Conexion as CON:
        with CON.cursor() as CURSOR:
            sentencia = 'UPDATE ESTUDIANTES Set nombre = %s, apellido = %s, email = %s, edad = %s, telefono = %s WHERE id_estudiante = %s'
            valores = ('Enrique', 'PC', 'Actualiza@prueba.com', 24, 1)
            CURSOR.execute(sentencia, valores)
            registro = CURSOR.rowcount
            print(f'Registro Actualizado: {registro}')
except Exception as ex:
    print(f'Error: {ex}')

finally:
    Conexion.close()