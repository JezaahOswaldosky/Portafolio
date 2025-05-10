import tkinter as tk 
from tkinter import filedialog, messagebox

## Creamos una funcion para un nuevo archivo 
def newFile(): 
    areaTexto.delete(1.0,tk.END)
    ventana.title("Bloc de Notas - Nuevo")

def openFile(): 
    ruta = filedialog.askopenfilename(
        filetypes=[("Archivos de texto","*.txt"), ("Toos los archivos", "*.*")]
    )
    if ruta: 
        with open(ruta, "r", encoding="utf-8") as archivo: 
            contenido  = archivo.read() 
            areaTexto.delete(1.0, tk.END)
            areaTexto.insert(tk.END, contenido)
            ventana.title(f"Bloc de Notas -  {ruta}")

def saveFile(): 
    ruta = filedialog.asksaveasfilename(
        defaultextension = ".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if ruta: 
        with open(ruta, "w", encoding="utf-8") as archivo: 
            contenido = areaTexto.get(1.0, tk.END)
            archivo.write(contenido)
            ventana.title(f"Bloc de Notas - {ruta}")

def salir(): 
    if messagebox.askokcancel("Salir", "Estas seguro de que deseas salir?"): 
        ventana.destroy() 
    
# Creamos la ventana principal 
ventana = tk.Tk()
ventana.title("Bloc de Notas")
ventana.geometry("600x400")
ventana.iconbitmap("Proyecto4_blockNote/cuaderno.ico") 

# Area de texto 
areaTexto = tk.Text(ventana, wrap="word", undo=True)
areaTexto.pack(expand=True, fill="both")

# Menu superior 
menuBarra = tk.Menu(ventana)

# Menu archivo 
menuArchivo = tk.Menu(menuBarra, tearoff=0)
menuArchivo.add_command(label="Nuevo", command=newFile)
menuArchivo.add_command(label="Abrir..", command=openFile)
menuArchivo.add_command(label="Guardar como..", command=saveFile)
menuArchivo.add_separator() 
menuArchivo.add_command(label="Salir", command=salir)

menuBarra.add_cascade(label="Archivo", menu= menuArchivo)

ventana.config(menu=menuBarra)

ventana.mainloop() 
