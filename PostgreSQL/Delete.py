import psycopg2 as db

Conexion = db.connect(user='postgres', password='admin20', host='127.0.0.1', port='5432', database='Escuela')

try:
    with Conexion as CON:
        with CON.cursor() as CURSOR:
            sentencia = 'DELETE FROM Estudiantes where id_estudiantes = %s'

            valores = (2, )

            CURSOR.execute(sentencia, valores)
            registro = CURSOR.rowcount
            print(f'Registro Eliminado: {registro}')
except Exception as ex:
    print(f'Error: {ex}')

finally:
    Conexion.close()