#Yes en ingles
name = "Hector"
last_name = "Garcia"
name = name + " " + last_name
print("Hello, " + name.title() +"!")
print("Hello," + name)
print(f"Hello, {name}")
age = 25
message = f"Happy {age} birthday"
print(message)
message = "Happy " + str(age) + " birthday"
print(message)
bikes = ["honda", "yamaha", "suzuki"]
print(bikes)
bikes.insert(3, "ducati")
print(bikes)
del bikes[0]
print("the best bike is:\n" + bikes[0].title())


