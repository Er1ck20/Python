
import psycopg2 as db

Conexion = db.connect(user='postgres', password='admin20', host='127.0.0.1', port='5432', database='Escuela')

# def Mostrar():
try:
    with Conexion as CON:
        with CON.cursor() as CURSOR:
            sentencia = 'Select * from Estudiantes'
            CURSOR.execute(sentencia)
            registro = CURSOR.fetchall()
            for registros in registro:
                print(registros)
except Exception as ex:
    print(f'Error: {ex}')

finally:
    Conexion.close()

