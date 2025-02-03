import mysql.connector

class CClientes:
    def __init__(self):
        # Establece la conexión a la base de datos
        self.conexion = mysql.connector.connect(
            host="127.0.0.1",  # Cambia a tu host
            user="root",    # Cambia a tu usuario
            password="admin",  # Cambia a tu contraseña
            database="clientesdb",  # Cambia a tu base de datos
            port=3306  # Cambia el puerto si es necesario
        )
        self.cursor = self.conexion.cursor()

    def mostrarClientes(self):
        try:
            # Realiza una consulta para obtener los clientes
            self.cursor.execute("SELECT ID, Nombres, Apellidos, Sexo FROM clientes")
            resultados = self.cursor.fetchall()  # Obtiene todos los resultados

            # Devuelve los resultados (una lista de tuplas)
            return resultados
        except Exception as e:
            print(f"Error al obtener los clientes: {e}")
            return []

    def IngresarClientes(self, nombres, apellidos, sexo):
        try:
            # Consulta SQL para insertar datos
            sql = "INSERT INTO clientes (nombres, apellidos, sexo) VALUES (%s, %s, %s)"
            valores = (nombres, apellidos, sexo)

            # Ejecuta la consulta
            self.cursor.execute(sql, valores)
            self.conexion.commit()  # Guarda los cambios

            print(f'{self.cursor.rowcount} registro(s) ingresado(s)')

        except mysql.connector.Error as error:
            print(f"Error al ingresar los datos: {error}")
