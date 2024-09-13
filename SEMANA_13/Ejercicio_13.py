import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para agregar un registro a la tabla
def agregar_dato():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    edad = entrada_edad.get()

    if nombre and apellido and edad.isdigit():
        tabla_datos.insert("", tk.END, values=(nombre, apellido, edad))
        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_edad.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese datos válidos. Asegúrese de que la edad sea un número.")

# Función para limpiar la tabla de datos
def limpiar_tabla():
    for item in tabla_datos.get_children():
        tabla_datos.delete(item)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema Para Agregrar de Johnny G")  # Título descriptivo
ventana.geometry("600x600")  # Tamaño de la ventana
ventana.config(bg="medium aquamarine")

# Estilo para centrar el texto en la tabla
style = ttk.Style()
style.configure("Treeview.Heading", anchor="center")  # Centrar encabezados
style.configure("Treeview", rowheight=25)  # Ajustar altura de las filas
style.configure("mystyle.Treeview", anchor="center")  # Centrar contenido

# Etiquetas y campos de texto
label_nombre = tk.Label(ventana, text="Ingrese su Nombre:", font=("Arial", 10))
label_nombre.pack(pady=5)
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack()

label_apellido = tk.Label(ventana, text="Ingrese su Apellido:", font=("Arial", 10))
label_apellido.pack(pady=5)
entrada_apellido = tk.Entry(ventana, width=30)
entrada_apellido.pack()

label_edad = tk.Label(ventana, text="Ingrese su Edad:", font=("Arial", 10))
label_edad.pack(pady=5)
entrada_edad = tk.Entry(ventana, width=30)
entrada_edad.pack()

# Botón para agregar los datos
boton_agregar = tk.Button(ventana,
                          text="Agregar",
                          font=("Arial", 12),
                          bg="green",
                          command=agregar_dato)
boton_agregar.pack(pady=10)

# Tabla (Treeview) para mostrar los datos
tabla_datos = ttk.Treeview(ventana, columns=("Nombre", "Apellido", "Edad"), show="headings", style="mystyle.Treeview")
tabla_datos.heading("Nombre", text="Nombre")
tabla_datos.heading("Apellido", text="Apellido")
tabla_datos.heading("Edad", text="Edad")

# Configurar el ancho de las columnas y centrar su contenido
tabla_datos.column("Nombre", anchor="center", width=100)
tabla_datos.column("Apellido", anchor="center", width=100)
tabla_datos.column("Edad", anchor="center", width=50)
tabla_datos.pack(pady=10)

# Botón para limpiar la tabla
boton_limpiar = tk.Button(ventana,
                          text="Limpiar",
                          font=("Arial", 12),
                          bg="yellow",
                          command=limpiar_tabla)
boton_limpiar.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
