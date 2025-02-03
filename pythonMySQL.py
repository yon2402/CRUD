import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

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

    # Mostrar clientes en el Treeview
    def mostrarClientes(self):
        try:
            self.cursor.execute("SELECT * FROM usuarios;")  # Cambié 'usuario' por 'usuarios'
            resultados = self.cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error al obtener los clientes: {e}")
            return []

    # Ingresar un nuevo cliente
    def IngresarClientes(self, nombres, apellidos, sexo):
        try:
            sql = "INSERT INTO usuarios (nombres, apellidos, sexo) VALUES (%s, %s, %s)"  # Cambié 'usuario' por 'usuarios'
            valores = (nombres, apellidos, sexo)
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            print(f'{self.cursor.rowcount} registro(s) ingresado(s)')
        except mysql.connector.Error as error:
            print(f"Error al ingresar los datos: {error}")

    # Modificar los datos de un cliente
    def ModificarClientes(self, cliente_id, nombre, apellidos, sexo):
        try:
            sql = "UPDATE usuarios SET nombres = %s, apellidos = %s, sexo = %s WHERE id = %s"  # Cambié 'usuario' por 'usuarios'
            valores = (nombre, apellidos, sexo, cliente_id)
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            print(f'{self.cursor.rowcount} registro(s) actualizado(s)')
        except mysql.connector.Error as error:
            print(f"Error al actualizar los datos: {error}")

    # Eliminar un cliente
    def EliminarCliente(self, cliente_id):
        try:
            sql = "DELETE FROM usuarios WHERE id = %s"  # Cambié 'usuario' por 'usuarios'
            self.cursor.execute(sql, (cliente_id,))
            self.conexion.commit()
            print(f'{self.cursor.rowcount} registro(s) eliminado(s)')
        except mysql.connector.Error as error:
            print(f"Error al eliminar los datos: {error}")


class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD de Clientes")
        self.root.geometry("600x500")

        # Inicializa la clase de clientes
        self.cliente = CClientes()

        # Frame principal
        self.groupBox = LabelFrame(self.root, text="Formulario de Cliente", padx=10, pady=10)
        self.groupBox.pack(padx=10, pady=10)

        # Campos para ingresar datos
        Label(self.groupBox, text="ID:").grid(row=0, column=0)
        self.textboxID = Entry(self.groupBox, width=25)
        self.textboxID.grid(row=0, column=1)

        Label(self.groupBox, text="Nombre:").grid(row=1, column=0)
        self.textboxNombre = Entry(self.groupBox, width=25)
        self.textboxNombre.grid(row=1, column=1)

        Label(self.groupBox, text="Apellido:").grid(row=2, column=0)
        self.textboxApellido = Entry(self.groupBox, width=25)
        self.textboxApellido.grid(row=2, column=1)

        Label(self.groupBox, text="Sexo:").grid(row=3, column=0)
        self.comboSexo = ttk.Combobox(self.groupBox, values=["Masculino", "Femenino", "Otro"])
        self.comboSexo.grid(row=3, column=1)

        # Botones
        self.btnGuardar = Button(self.groupBox, text="Guardar", width=15, command=self.GuardarCliente)
        self.btnGuardar.grid(row=4, column=0, padx=5, pady=10)

        self.btnModificar = Button(self.groupBox, text="Modificar", width=15, command=self.ModificarCliente)
        self.btnModificar.grid(row=4, column=1, padx=5, pady=10)

        self.btnEliminar = Button(self.groupBox, text="Eliminar", width=15, command=self.EliminarCliente)
        self.btnEliminar.grid(row=4, column=2, padx=5, pady=10)

        # Treeview para mostrar clientes
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Apellido", "Sexo"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Sexo", text="Sexo")
        self.tree.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # Cargar clientes al Treeview
        self.actualizarTreeview()

    # Función para mostrar clientes en el Treeview
    def actualizarTreeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        clientes = self.cliente.mostrarClientes()
        for cliente in clientes:
            self.tree.insert("", "end", values=cliente)

    # Función para guardar cliente
    def GuardarCliente(self):
        nombre = self.textboxNombre.get().strip()
        apellido = self.textboxApellido.get().strip()
        sexo = self.comboSexo.get().strip()

        if not nombre or not apellido or not sexo:
            messagebox.showerror('Error', 'Todos los campos son obligatorios')
            return

        self.cliente.IngresarClientes(nombre, apellido, sexo)
        messagebox.showinfo('Información', 'Cliente guardado correctamente')
        self.actualizarTreeview()
        self.LimpiarCampos()

    # Función para modificar cliente
    def ModificarCliente(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Debes seleccionar un cliente para modificar")
            return

        item_values = self.tree.item(selected_item, "values")
        cliente_id = item_values[0]
        nombre = item_values[1]
        apellidos = item_values[2]
        sexo = item_values[3]

        self.textboxID.delete(0, END)
        self.textboxID.insert(0, cliente_id)
        self.textboxNombre.delete(0, END)
        self.textboxNombre.insert(0, nombre)
        self.textboxApellido.delete(0, END)
        self.textboxApellido.insert(0, apellidos)
        self.comboSexo.set(sexo)

        def GuardarModificaciones():
            nuevo_nombre = self.textboxNombre.get().strip()
            nuevo_apellido = self.textboxApellido.get().strip()
            nuevo_sexo = self.comboSexo.get().strip()

            if not nuevo_nombre or not nuevo_apellido or not nuevo_sexo:
                messagebox.showerror('Error', 'Todos los campos son obligatorios')
                return

            self.cliente.ModificarClientes(cliente_id, nuevo_nombre, nuevo_apellido, nuevo_sexo)
            messagebox.showinfo('Información', 'Los datos fueron modificados correctamente')
            self.actualizarTreeview()
            self.LimpiarCampos()

        # Botón para guardar modificaciones
        btnGuardarModificaciones = Button(self.groupBox, text="Guardar Modificaciones", width=15, command=GuardarModificaciones)
        btnGuardarModificaciones.grid(row=5, column=1, padx=5, pady=10)

    # Función para eliminar cliente
    def EliminarCliente(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Debes seleccionar un cliente para eliminar")
            return

        item_values = self.tree.item(selected_item, "values")
        cliente_id = item_values[0]

        confirmacion = messagebox.askyesno("Confirmación", f"¿Estás seguro de que quieres eliminar el cliente con ID: {cliente_id}?")
        if confirmacion:
            self.cliente.EliminarCliente(cliente_id)
            messagebox.showinfo("Información", "Cliente eliminado correctamente")
            self.actualizarTreeview()

    # Limpiar los campos
    def LimpiarCampos(self):
        self.textboxID.delete(0, END)
        self.textboxNombre.delete(0, END)
        self.textboxApellido.delete(0, END)
        self.comboSexo.set('')


if __name__ == "__main__":
    root = Tk()
    interfaz = Interfaz(root)
    root.mainloop()
