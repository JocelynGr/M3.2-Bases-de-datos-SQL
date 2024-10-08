import mysql.connector
import pandas as pd
from mysql.connector import Error


def create_connection():
    """ Crea una conexión con la base de datos MySQL. """
    try:
        connection = mysql.connector.connect(
            host='195.179.238.58',  # Cambia esto a tu host
            user='u927419088_admin',  # Cambia esto a tu usuario
            password='#Admin12345#',  # Cambia esto a tu contraseña
            database='u927419088_testing_sql'  # Cambia esto al nombre de tu base de datos
        )

        if connection.is_connected():
            print('Conexión exitosa a la base de datos MySQL')
            return connection

    except Error as e:
        print(f'Error al conectar a MySQL: {e}')
        return None


def update_data(connection):
    """ Ejecuta una consulta de actualización en la tabla 'curso'. """
    try:
        cursor = connection.cursor()
        query = "UPDATE curso SET nombreDescriptivo='Tercero' WHERE idCurso=3"
        cursor.execute(query)
        connection.commit()
        print('Datos actualizados correctamente')

    except Error as e:
        print(f'Error al ejecutar la consulta de actualización: {e}')


def fetch_data(connection):
    """ Consulta los registros de la tabla 'curso' y devuelve un DataFrame. """
    try:
        query = "SELECT * FROM curso"
        df = pd.read_sql(query, connection)
        return df

    except Error as e:
        print(f'Error al ejecutar la consulta: {e}')
        return None


def export_to_excel(df, filename):
    """ Exporta el DataFrame a un archivo Excel. """
    try:
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f'Datos exportados a {filename}')

    except Exception as e:
        print(f'Error al exportar a Excel: {e}')


# Usa las funciones
connection = create_connection()

if connection:
    update_data(connection)  # Actualiza los datos
    df = fetch_data(connection)  # Obtiene los datos actualizados
    if df is not None:
        export_to_excel(df, 'cursos.xlsx')

    connection.close()
