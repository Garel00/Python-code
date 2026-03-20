import math

class Dog():
    """A dog age calculator."""
    
    def __init__(self, name, age, owner):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.owner = owner
    

    def calculate_age(self):
        """Calculate my dog age"""
        age = round(16*math.log(self.age) + 20, 1)
        print(f"\nLa edad perruna de {self.name.title()} es: {age}")

    def call_owner(self):
        """Call owner"""
        print(f"{self.owner.title()} es el mejor amigo de {self.name.title()}")

    def bark(self):
        """Dog will bark"""
        print(f"{self.name.title()} dice woof woof!!!\n")

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

