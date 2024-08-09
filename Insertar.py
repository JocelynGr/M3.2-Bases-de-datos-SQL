import mysql.connector
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


def insert_data(connection, nombre_descriptivo, n_asignatura):
    """ Inserta un nuevo registro en la tabla 'curso'. """
    try:
        cursor = connection.cursor()
        query = "INSERT INTO curso (idCurso,nombreDescriptivo, nAsignaturas) VALUES (%s,%s, %s)"
        values = (15,'Octavo', 5)
        cursor.execute(query, values)
        connection.commit()
        print(f'Registro insertado: nombreDescriptivo={nombre_descriptivo}, nAsignatura={n_asignatura}')

    except Error as e:
        print(f'Error al insertar el registro: {e}')
        connection.rollback()


# Usa las funciones
connection = create_connection()

if connection:
    # Insertar un nuevo registro
    insert_data(connection, 'Nuevo Curso', 5)  # Cambia estos valores según lo necesites

    connection.close()
