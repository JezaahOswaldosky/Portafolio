import tkinter as tk 
from datetime import datetime
import time
import threading

## Crear la ventana principal 
ventana = tk.Tk() 
ventana.title("Reloj Digital Simple")
ventana.iconbitmap("Proyecto5_DigitalClock/clockIcon.ico")
ventana.geometry("300x300")

## Etiqueta para mostrar el tiempo 
label = tk.Label(ventana, text = "", font=("Arial", 30))
label.pack(pady=20)

## Variable de modo: reloj, cronometro o tempoerizador 
modo =tk.StringVar(value="reloj")

# =========== Modo Reloj 
def mostrarReloj(): 
    if modo.get() == "reloj": 
        ahora = datetime.now().strftime("%H:%M:%S")
        label.config(text=ahora)
    ventana.after(1000, mostrarReloj)

    ## ============Modo Cronometro
cronometroActivado = False 
tiempoCronometro = 0 

def iniciarCrono(): 
    global cronometroActivado, tiempoCronometro
    cronometroActivado = True 
    while cronometroActivado and modo.get() == "cronometro" : 
        minutos, segundos =  divmod(tiempoCronometro, 60)
        label.config(text=f"{minutos: 02}:{segundos: 02}")
        tiempoCronometro += 1
        time.sleep(1)

def toggleCronometro(): 
    global cronometroActivado, tiempoCronometro
    if not cronometroActivado: 
        modo.set("cronometro")
        tiempoCronometro = 0
        threading.Thread(target=iniciarCrono, daemon=True).start()
    else: 
        cronometroActivado = False

##  ============= Modo Temporizador
def iniciarTemporizador(): 
    try: 
        segundos = int(entrada.get())
        modo.set("temporizador")
        threading.Thread(target=temporizador, args=(segundos,), daemon=True).start() 
    except ValueError: 
        label.config(text="Numero invalido")

def temporizador(segundos): 
    while segundos >= 0 and modo.get() == "temporizador": 
        m,s = divmod(segundos, 60)
        label.config(text=f"{m:02}:{s:02}")
        time.sleep(1)
        segundos -= 1 
    if segundos < 0: 
        label.config(text="Tiempo!!")
    
## =========  Botones
frameBotones =  tk.Frame(ventana)
frameBotones.pack(pady=10)

tk.Button(frameBotones, text="Reloj", command=lambda: modo.set("reloj")).grid(row=0, column=0, padx=5)
tk.Button(frameBotones, text="Cronometro", command=toggleCronometro).grid(row=0, column=1, padx=5)

# Entrada y boton para el temporizador 
entrada = tk.Entry(ventana, width=10, font=("Arial", 15))
entrada.pack(pady=5)
tk.Button(ventana, text="Iniciar Temporizador (Segundos)", command=iniciarTemporizador).pack()

# Mostrar la aplicacion 
mostrarReloj() 

# Iniciar la interfaz principal 
ventana.mainloop()
