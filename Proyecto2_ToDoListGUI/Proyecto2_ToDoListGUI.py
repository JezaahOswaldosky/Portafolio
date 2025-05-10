##                                      Proyecto2_ToDoList.py
##
## Proyecto2_ToDoList.py es una interfaz grafica de una lista de tarea. Que permite al usuario introducir 
#3 datos e informacion y se guarda hasta que este sea completado. 
###########################################################################################################
import tkinter as tk 
from tkinter import messagebox

def agregarTarea(): 
    tarea = entrada.get()
    if tarea != "": 
        listaTareas.insert(tk.END, tarea)
        entrada.delete(0,tk.END)
    else: 
        messagebox.showwarning("Advertencia", "Debes escribir una tarea!!")

def eliminarTarea(): 
    try: 
        indice = listaTareas.curselection()[0]
        listaTareas.delete(indice)
    except IndexError: 
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Crear ventana principal 
ventana = tk.Tk() 
ventana.title("Lista de tareas")
ventana.iconbitmap("Proyecto2_ToDoListGUI/ToDoList.ico")
ventana.geometry("300x400")
ventana.resizable(False, False)

# Entrada de texto para nuevas tareas 
entrada = tk.Entry(ventana, width=25, font=("Arial", 14))
entrada.pack(pady=10)

# Boton para agregar tareas 
botonAgregar = tk.Button(ventana, text="Agregar Tarea", width=20, command=agregarTarea)
botonAgregar.pack(pady=5)

# Lista de tareas 
listaTareas = tk.Listbox(ventana, width=30, height=10, font=("Arial", 12), selectbackground="lightblue")
listaTareas.pack(pady=10)

## Boton para eliminar tareas 
boton_Eliminar = tk.Button(ventana, text="Eliminar tarea", width=20, command=eliminarTarea)
boton_Eliminar.pack(pady=5)

# Ejecutar la aplicacion 
ventana.mainloop()
