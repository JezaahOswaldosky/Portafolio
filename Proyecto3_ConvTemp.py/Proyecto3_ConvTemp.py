import tkinter as tk
from tkinter import ttk

# Función para convertir temperaturas
def convertir():
    try:
        valor = float(entrada.get())
        de = unidad_origen.get()
        a = unidad_destino.get()
        
        # Convertir primero a Celsius
        if de == "Celsius":
            c = valor
        elif de == "Fahrenheit":
            c = (valor - 32) * 5/9
        elif de == "Kelvin":
            c = valor - 273.15

        # Convertir de Celsius a destino
        if a == "Celsius":
            resultado = c
        elif a == "Fahrenheit":
            resultado = c * 9/5 + 32
        elif a == "Kelvin":
            resultado = c + 273.15
        
        salida_var.set(f"{resultado:.2f} {a}")
    except ValueError:
        salida_var.set("Entrada no válida")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Temperatura")
ventana.geometry("300x200")

# Entrada de temperatura
tk.Label(ventana, text="Temperatura:").pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack()

# Menú desplegable de unidades
opciones = ["Celsius", "Fahrenheit", "Kelvin"]

unidad_origen = ttk.Combobox(ventana, values=opciones, state="readonly")
unidad_origen.set("Celsius")
unidad_origen.pack(pady=5)

unidad_destino = ttk.Combobox(ventana, values=opciones, state="readonly")
unidad_destino.set("Fahrenheit")
unidad_destino.pack(pady=5)

# Botón de conversión
tk.Button(ventana, text="Convertir", command=convertir).pack(pady=10)

# Resultado
salida_var = tk.StringVar()
tk.Label(ventana, textvariable=salida_var, font=("Arial", 12)).pack(pady=5)

ventana.mainloop()
