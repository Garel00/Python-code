import math

def suma_operation(num1, num2):
    suma = num1 + num2
    print(f"El resultado de la suma es {suma}\n")

def resta_operation(num1, num2):
    resta = num1 - num2
    print(f"El resultado de la resta es {resta}\n")

def division_operation(num1, num2):
    while True:
        division = num1/num2
        print(f"El resultado de la division es {division}\n")


while True:
    try:
        option = int(input("Que operacion quieres realizar? \n 1. Suma \n 2. Resta \n 3. Division\n"))
        
        if option == 4:
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        if option not in [1, 2 ,3]:
            print("Opcion no valida")
            continue
        num1 = float(input("ingrese el primer numero\n"))
        num2 = float(input("ingrese el segundo numero\n"))
        if option == 1:
            suma_operation(num1, num2)
        elif option == 2:
            resta_operation(num1, num2)
        elif option == 3:
            division_operation(num1, num2)
        else:
            print("Opcion no valida.\n")
    except ValueError:
        print("\n==============================================\n")
        print("Eso no es un numero valido, intente de nuevo por favor... \n")
        print("==============================================\n")