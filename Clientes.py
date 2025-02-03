import mysql.connector

class CClientes:
    def __init__(self):
        try:
            # Establece la conexión a la base de datos
            self.conexion = mysql.connector.connect(
                host="127.0.0.1",  # Cambia a tu host
                user="root",        # Cambia a tu usuario
                password="admin",   # Cambia a tu contraseña
                database="clientesdb",  # Cambia a tu base de datos
                port=3306           # Cambia el puerto si es necesario
            )
            self.cursor = self.conexion.cursor()
        except mysql.connector.Error as error:
            print(f"Error al conectar a la base de datos: {error}")

    def mostrarClientes(self):
        try:
            # Realiza una consulta para obtener los clientes
            self.cursor.execute("select * from usuarios;")
            resultados = self.cursor.fetchall()  # Obtiene todos los resultados
            return resultados
        except mysql.connector.Error as e:
            print(f"Error al obtener los clientes: {e}")
            return []

    def IngresarClientes(self, nombres, apellidos, sexo):
        try:
            # Consulta SQL para insertar datos
            sql = "INSERT INTO usuarios (nombres, apellidos, sexo) VALUES (%s, %s, %s)"
            valores = (nombres, apellidos, sexo)

            # Ejecuta la consulta
            self.cursor.execute(sql, valores)
            self.conexion.commit()  # Guarda los cambios

            print(f'{self.cursor.rowcount} registro(s) ingresado(s)')

        except mysql.connector.Error as error:
            print(f"Error al ingresar los datos: {error}")

    def cerrarConexion(self):
        try:
            # Cierra la conexión y el cursor
            self.cursor.close()
            self.conexion.close()
            print("Conexión cerrada correctamente.")
        except mysql.connector.Error as error:
            print(f"Error al cerrar la conexión: {error}")

# Prueba de la clase
if __name__ == "__main__":
    cliente = CClientes()
    
    # Insertar un cliente (modifica con datos reales)
    cliente.IngresarClientes("Juan", "Pérez", "Masculino")
    
    # Mostrar clientes
    clientes = cliente.mostrarClientes()
    for cliente in clientes:
        print(cliente)
    
    # Cerrar la conexión después de realizar las operaciones
    cliente.cerrarConexion()
