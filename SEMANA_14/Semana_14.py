"""Desarrollar una aplicación GUI utilizando Tkinter en Python que funcione como una agenda personal.
 La aplicación permitirá al usuario agregar, ver, y eliminar eventos o tareas programadas."""

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


# Creamos nuestra clase principal que maneja la aplicación de la agenda
class AgendaApp:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Agenda Personal")  # Título de la ventana
        self.root.geometry("600x600")  # Tamaño de la ventana
        self.root.config(bg="midnight blue")  # Color de fondo de la ventana

        # Frame para la entrada de datos (se crea antes de la lista de eventos)
        frame_entrada = tk.Frame(self.root)
        frame_entrada.pack(padx=15, pady=15)  # Padding del frame para mantener espacio alrededor

        # Etiqueta y campo de entrada para la fecha
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=5)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada para la hora
        tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(frame_entrada)  # Campo de texto para ingresar la hora
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada para la descripción del evento
        tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_entrada)  # Campo de texto para ingresar la descripción
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones de control
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(padx=10, pady=10)

        # Botón para agregar un evento a la lista
        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5, pady=5)

        # Botón para eliminar el evento seleccionado en la lista
        tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT,
                                                                                                         padx=5, pady=5)

        # Botón para salir de la aplicación
        tk.Button(frame_botones, text="Salir", command=self.root.quit).pack(side=tk.LEFT, padx=5, pady=5)

        # Frame para la lista de eventos, ubicado al final
        frame_lista = tk.Frame(self.root)
        frame_lista.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)  # Se expande para llenar el espacio disponible

        # Treeview para mostrar los eventos en una tabla
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")

        # Configuración de las columnas para mostrar los datos centrados
        self.tree.column("Fecha", anchor="center", width=100)  # Columna de fecha centrada
        self.tree.column("Hora", anchor="center", width=100)  # Columna de hora centrada
        self.tree.column("Descripción", anchor="center", width=200)  # Columna de descripción centrada

        # Encabezados de las columnas también centrados
        self.tree.heading("Fecha", text="Fecha", anchor="center")
        self.tree.heading("Hora", text="Hora", anchor="center")
        self.tree.heading("Descripción", text="Descripción", anchor="center")

        # Empaquetar el Treeview para que ocupe todo el espacio disponible
        self.tree.pack(fill=tk.BOTH, expand=True)

    # Método para agregar un evento a la lista
    def agregar_evento(self):
        # Obtener los datos de los campos de entrada
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        # Validar que todos los campos estén completos
        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Alerta del sistema",
                                   "Por favor, rellena todos los campos.")  # Mostrar advertencia si faltan datos
            return

        # Agregar el evento al Treeview (tabla de eventos)
        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar los campos de entrada después de agregar el evento
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    # Método para eliminar el evento seleccionado de la lista
    def eliminar_evento(self):
        # Obtener el evento seleccionado
        seleccion = self.tree.selection()

        if seleccion:
            # Preguntar al usuario si está seguro de eliminar el evento
            confirmar = messagebox.askyesno("Confirmar eliminación", "¿Seguro que quieres eliminar este evento?")
            if confirmar:
                # Eliminar el evento del Treeview si se confirma
                self.tree.delete(seleccion)
        else:
            # Mostrar advertencia si no hay un evento seleccionado
            messagebox.showwarning("Seleccionar evento", "Por favor, selecciona un evento para eliminar.")


# Crear la ventana principal
root = tk.Tk()

# Iniciar la aplicación creando una instancia de la clase AgendaApp
app = AgendaApp(root)

# Ejecutar el loop principal de la aplicación
root.mainloop()
