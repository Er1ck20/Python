# Importamos el modulo de psycopg2
import psycopg2 

# Realizamos la conexion
Conexion = psycopg2.connect(user='postgres', password='ejemplo', host='127.0.0.1', port='5432', database= 'ejemplo')

# Manejo de excepciones
try:
    with Conexion:
        with Conexion.cursor() as cursor:
            # Sentencia SQL
            sentencia = 'SELECT * FROM empleado'
            # Ejecutamos la sentencia
            cursor.execute(sentencia)
            # fetchall() - Sirve para buscar los registros
            registro = cursor.fetchall() 
            # Bucle for
            for registros in registro:
                print(registros)
            
except Exception as ex:
    print(f'ERROR: {ex}')

finally:
    Conexion.close()
