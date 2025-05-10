##                                      Proyecto1_CalculadoraGUI.py 
##
## Proyecto1_CalculadoraGUI.py es un programa de interfaz grafico que permite sumar y tener botones como 
## una aplicacion de calculadora. Proyecto sencillo pero eficaz y muy divertido de hacer y usar. 
##########################################################################################################
import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.expresion = ""
        self.entrada_texto = tk.StringVar()

        # Configuración de la ventana principal
        root.title("Calculadora")
        root.geometry("420x445")
        root.iconbitmap("Proyecto1_CalculadoraGUI/calcular.ico") 
        root.resizable(False, False) 

        # Campo de entrada
        entrada = tk.Entry(root, textvariable=self.entrada_texto, font=('Arial', 20), bd=10, insertwidth=2, width=14,
                           borderwidth=4, relief='ridge', justify='right')
        entrada.grid(row=0, column=0, columnspan=4)

        # Botones
        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 4)  # Botón igual ocupa toda la fila
        ]

        for boton in botones:
            texto = boton[0]
            fila = boton[1]
            columna = boton[2]
            colspan = boton[3] if len(boton) == 4 else 1

            b = tk.Button(root, text=texto, padx=20, pady=20, font=('Arial', 14), bd=4, width=5, height=1,
                          command=lambda t=texto: self.click(t))
            b.grid(row=fila, column=columna, columnspan=colspan, sticky="nsew")

    def click(self, item):
        if item == "C":
            self.expresion = ""
        elif item == "=":
            try:
                self.expresion = str(eval(self.expresion))
            except Exception:
                self.expresion = "Error"
        else:
            self.expresion += str(item)

        self.entrada_texto.set(self.expresion)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
