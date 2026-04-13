#Project Euler Problem 9
import math
#Se despeja la 2da y tercera ecuacion y obtenemos b = 1000 - 500000/(1000-a)
#De la inecuacion 1 sabemos que a < b < c, a no debe ser mayor a una tercera parte de 1000
for i in range(1, 332):
    r = 500000 % (1000 - i)
    if r == 0:
        a = i
b = 1000 - 500000 / (1000 - a)
c = 1000 - b - a
list = [a, b, c]
print(f"Los resultados a, b y c son: {list}")