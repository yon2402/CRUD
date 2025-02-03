import mysql.connector

class CConexion:
    @staticmethod
    def ConexionBaseDeDatos():
        print("Intentando conectar...")  # Mensaje para verificar si la función se llama
        try:
            # Aquí haces la conexión a la base de datos
            connection = mysql.connector.connect(
                host="127.0.0.1",  # Cambia esto según tu configuración
                user="root",  # Cambia esto según tu configuración
                password="admin",  # Cambia esto según tu configuración
                database="clientesdb",  # Cambia esto según tu base de datos
                port=3306  # Especifica el puerto
            )
            print("Conexión exitosa a la base de datos.")  # Agregado para depuración
            return connection
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            return None


