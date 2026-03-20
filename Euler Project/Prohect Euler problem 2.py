##Prohect Euler problem 2
##Fibonacci numbers
x = 1
x1 = 2
suma = 0
while x1 < 4000000:
    if x1 % 2 == 0:
        suma += x1
    x = x1
    x1 = suma
print(suma)
