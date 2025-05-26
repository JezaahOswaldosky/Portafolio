###                 Programa5.py 
###
### Programa5.py es un programa que toma un texto y esta la 
### lo encripta mediante el algoritmo cesar. 
### 1. Pedir frase al usuario 
### 2. Convertir texto a numerico 
### 3. Simar _1 a cada caracter 
### 4. Convertir de numerico a texto 
### 5. Mostrar el texto encriptado
##############################################################
parrafo =  input("Introduce un texto: ")
parraforNum = [ord(c) for c in parrafo]

## Debug 
print(f"\n\n{parraforNum}\n")
