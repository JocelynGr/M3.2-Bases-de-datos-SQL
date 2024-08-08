import mysql.connector
from mysql.connector import Error

def create_connection():
    """ Crea una conexión con la base de datos MySQL. """
    try:
        # Establece la conexión con la base de datos
        connection = mysql.connector.connect(
            host='195.179.238.58',       # Cambia esto a tu host
            user='u927419088_admin',            # Cambia esto a tu usuario
            password='#Admin12345#',    # Cambia esto a tu contraseña
            database='u927419088_testing_sql'   # Cambia esto al nombre de tu base de datos
        )

        if connection.is_connected():
            print('Conexión exitosa a la base de datos MySQL')
            return connection

    except Error as e:
        print(f'Error al conectar a MySQL: {e}')
        return None

def close_connection(connection):
    """ Cierra la conexión con la base de datos. """
    if connection.is_connected():
        connection.close()
        print('Conexión cerrada')

# Usa las funciones
connection = create_connection()

# Realiza operaciones con la base de datos aquí

close_connection(connection)
