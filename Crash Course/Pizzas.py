pizzas = ["pepperoni", "margarita", "cheese"]
print("My favorite pizzas are:")
position = 1
for pizza in pizzas:
    print(f"{position}. {pizza.title()}")
    position += 1
print("For me, these are the best pizzas")

my_food = ["pizza", "falafel", "carrot cake"]
friend_food = my_food[:]


used_usernames = ["Mjolnir", "Gungnir", "Leviathan"]
requested_usernames = ["Mjolnir", "Chief"]
for requested_username in requested_usernames:
    if requested_username in used_usernames:
        print(f"Sorry, {requested_username} is already being used.")
    else:
        print(f"\nWelcome, {requested_username}")


armors = [{"model": "Mark 5", "Color": "Green", "Material": "Titanium"}, {"model": "Mark 4", "Color": "Gray", "Material": "Titanium"}, 
          {"model": "Mark 5", "Color": "Blue", "Material": "Titanium"}]
armor_number = 1
print("Armors available:")
print("---------------------")
for armor in armors:
    print(f"{armor_number}.\nModel: {armor["model"]}")
    print(f"Color: {armor['Color']}")
    print(f"Material: {armor['Material']}")
    print("---------------------")
    armor_number += 1

print(armors[1]["model"])