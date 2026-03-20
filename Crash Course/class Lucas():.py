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
        age = 16*math.log(self.age) + 20
        print(f"{self.name.title()} age is: {age}")

    def call_owner(self):
        """Call owner"""
        print(f"{self.owner.title()} is the {self.name.title()} owner")



my_dog = Dog("lucas", 10, "lalo")
my_dog.calculate_age()
my_dog.call_owner()

print("\n")
Danias_dog = Dog("boomer", 8, "Dania")
Danias_dog.calculate_age()
Danias_dog.call_owner()

print("\n")
mane1_dog = Dog("Canelo", 13, "Mane")
mane1_dog.calculate_age()
mane1_dog.call_owner()

print("\n")
mane2_dog = Dog("Hulk", 9, "Mane")
mane2_dog.calculate_age()
mane2_dog.call_owner()

print("\n")
mane3_dog = Dog("Bola", 7, "Mane")
mane3_dog.calculate_age()
mane3_dog.call_owner()

print("\n")
mane4_dog = Dog("Others", 6, "Mane")
mane4_dog.calculate_age()
mane4_dog.call_owner()