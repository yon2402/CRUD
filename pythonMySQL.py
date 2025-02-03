import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Clientes import CClientes

class FormularioClientes:
    def __init__(self):
        self.base = None
        self.textboxID = None
        self.textboxNombre = None
        self.textboxApellido = None
        self.comboSexo = None
        self.tree = None
        self.groupBox = None

    def Formulario(self):
        try:
            self.base = Tk()
            self.base.geometry("1200x300")  # Ajuste del tamaño
            self.base.title("Formulario Python")

            # Crear el GroupBox (LabelFrame)
            self.groupBox = LabelFrame(self.base, text="Datos del Personal", padx=10, pady=10)
            self.groupBox.grid(row=0, column=0, padx=10, pady=10)

            # Campo ID
            labelID = Label(self.groupBox, text="ID:", width=13, font=("Arial", 12))
            labelID.grid(row=0, column=0, padx=5, pady=5)
            self.textboxID = Entry(self.groupBox)
            self.textboxID.grid(row=0, column=1, padx=5, pady=5)

            # Campo Nombre
            labelNombre = Label(self.groupBox, text="Nombre:", width=13, font=("Arial", 12))
            labelNombre.grid(row=1, column=0, padx=5, pady=5)
            self.textboxNombre = Entry(self.groupBox)
            self.textboxNombre.grid(row=1, column=1, padx=5, pady=5)

            # Campo Apellido
            labelApellido = Label(self.groupBox, text="Apellido:", width=13, font=("Arial", 12))
            labelApellido.grid(row=2, column=0, padx=5, pady=5)
            self.textboxApellido = Entry(self.groupBox)
            self.textboxApellido.grid(row=2, column=1, padx=5, pady=5)

            # Campo Sexo (usando Combobox)
            labelSexo = Label(self.groupBox, text="Sexo:", width=13, font=("Arial", 12))
            labelSexo.grid(row=3, column=0, padx=5, pady=5)
            self.comboSexo = ttk.Combobox(self.groupBox, values=["Masculino", "Femenino"])
            self.comboSexo.grid(row=3, column=1, padx=5, pady=5)

            # Botones
            btnGuardar = Button(self.groupBox, text="Guardar", width=10, command=self.GuardarRegistros)
            btnGuardar.grid(row=4, column=0, padx=5, pady=10)

            btnModificar = Button(self.groupBox, text="Modificar", width=10)
            btnModificar.grid(row=4, column=1, padx=5, pady=10)

            btnEliminar = Button(self.groupBox, text="Eliminar", width=10)
            btnEliminar.grid(row=4, column=2, padx=5, pady=10)

            # Crear otro LabelFrame para la lista
            groupBoxLista = LabelFrame(self.base, text="Lista", padx=5, pady=5)
            groupBoxLista.grid(row=0, column=1, padx=5, pady=5)

            # Crear la tabla (Treeview)
            self.tree = ttk.Treeview(groupBoxLista, columns=("ID", "Nombres", "Apellidos", "Sexo"), show='headings', height=5)

            # Configurar columnas
            self.tree.column("ID", anchor=CENTER, width=100)
            self.tree.column("Nombres", anchor=CENTER, width=150)
            self.tree.column("Apellidos", anchor=CENTER, width=150)
            self.tree.column("Sexo", anchor=CENTER, width=100)

            # Configurar encabezados
            self.tree.heading("ID", text="ID")
            self.tree.heading("Nombres", text="Nombres")
            self.tree.heading("Apellidos", text="Apellidos")
            self.tree.heading("Sexo", text="Sexo")

            # Mostrar la tabla
            for row in CClientes().mostrarClientes():
                print(row)
                self.tree.insert("", "end", values=row)

            # Posicionar la tabla
            self.tree.grid(row=5, column=0, columnspan=3, padx=5, pady=10)

            self.base.mainloop()
        except Exception as error:
            print(f'Error al mostrar la interfaz, error: {error}')

    def GuardarRegistros(self):
        try:
            # Verificar si los campos están inicializados
            if self.textboxNombre is None or self.textboxApellido is None or self.comboSexo is None:
                print("Error: Elementos de la interfaz no inicializados")
                return

            nombre = self.textboxNombre.get().strip()
            apellidos = self.textboxApellido.get().strip()
            sexo = self.comboSexo.get().strip()

            if not nombre or not apellidos or not sexo:
                messagebox.showerror('Error', 'Todos los campos son obligatorios')
                return

            # Crear una instancia de CClientes e ingresar los datos
            cliente = CClientes()
            cliente.IngresarClientes(nombre, apellidos, sexo)

            messagebox.showinfo('Información', 'Los datos fueron guardados correctamente')

            # Limpiar los campos
            self.textboxNombre.delete(0, END)
            self.textboxApellido.delete(0, END)
            self.comboSexo.set('')

        except Exception as error:
            print(f'Error al ingresar los datos: {error}')
            messagebox.showerror('Error', f'Error al ingresar los datos: {error}')

# Crear una instancia de la clase y llamar al método
if __name__ == "__main__":
    form = FormularioClientes()
    form.Formulario()
