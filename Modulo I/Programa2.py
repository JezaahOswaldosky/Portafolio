###                 Programa2.py 
###
### Programa2.py pide el nombre y edad de un usuario para mostrar un 
### mensaje de texto como "Hola {nombre}, tienes {anio} anios" 
### 1. Pide nombre a usuario 
### 2. Pide edad al usuario 
### 3. Imprime mensaje "Hola {nombre}, tienes {anio} anios"
####################################################################################

## Pedir nombre y eadd del usuario
nombre = input("Nombre: ")
edad = int(input("Edad: "))

## Imprimir mensaje 
print(f"Hola {nombre}, tienes {edad} anios")
