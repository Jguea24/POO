import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas de Johnny G")
        self.root.config(bg="cadet blue")

        # Crear campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=60)
        self.task_entry.grid(row=0, column=0, padx=60, pady=60)
        self.task_entry.bind("<Return>", self.add_task)  # Añadir tarea con Enter

        # Crear botón para añadir tareas
        self.add_button = tk.Button(root, text="Añadir", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Crear Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(root, height=15, width=90, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Crear botones para "Marcar como Completada" y "Eliminar Tarea"
        self.complete_button = tk.Button(root, text="Marcar", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.delete_button = tk.Button(root, text="Eliminar", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Función para añadir una nueva tarea
    def add_task(self, event=None):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

    # Función para marcar una tarea como completada
    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            completed_task = f"{task} (Completada)"
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(tk.END, completed_task)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para completar.")

    # Función para eliminar una tarea
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")


# Configuración principal de la ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
