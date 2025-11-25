import math
from dog import Dog

while True:
  owner = input("Hola! Esta es una calculadora de edad perruna, por favor ingresa tu nombre para continuar. \n")
  name = input(f"Mucho gusto, {owner.title()}. Ingresa el nombre de tu perrhijo \n")

  while True:
      try:
        age = int(input("Ahora ingresa la edad de tu perrhijo \n"))
        if age <= 0:
            print("La edad debe ser un numero valido \n")
            continue
        break
      except ValueError:
          print("\n==============================================\n")
          print("Eso no es un numero valido, intente de nuevo por favor... \n")
          print("==============================================\n")
  
  my_dog = Dog(name, age, owner)
  print("==============================================")
  my_dog.calculate_age()
  my_dog.call_owner()
  my_dog.bark()
  print("==============================================\n")

  repeat = input("\n Quieres calcular la edad de otro perrunido? (si/no): \n").strip().lower()
  if repeat != 'si':
      print("\n==============================================\n")
      print("Gracias por usar la calculadora de edad perruna\n")
      print("==============================================")
      break

