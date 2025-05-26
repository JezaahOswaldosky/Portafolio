###                         CalBasic.py 
###
### CalBasic.py es un programa que permite al usuario introducir dos 
### numeros ya sean enteros o flotantes para aplicar su aritmetica 
### Pseudocodigo: 
### 1. Usuario introduce el primer numero 
### 2. El usuario introduce el tipo de aritmetica a realizar 
### 3. El usuario introduce el segundo numero 
### 4. Se imprime el numero 
######################################################################
ciclo = True

while ciclo: 
    # Mensaje introductorio 
    print("\t\t\t CalBasic.py")
    print("1. + Suma\n2. - Resta\n3. * Multiplicacion\n4. / Division")
    print("5. Salir o salir")
    num1 =  float(input("Introduce el numero A: "))
    aritmetica = input("Operador: ")
    num2 = float(input("Introduce el numero B: "))

    ### 
    if aritmetica == "+":
        print(f"Resultado: {num1+num2}")
    elif aritmetica == "-": 
        print(f"Resultado: {num1-num2}")
    elif aritmetica == "*": 
        print(f"Resultado: {num1*num2}")
    elif aritmetica == "/": 
        print(f"Resultado: {num1/num2}")
    elif aritmetica == "Salir"  or aritmetica == "salir":
        ciclo = False 
    else: 
        print("Esa opearcion no existe!!!")
