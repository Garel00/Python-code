#Project Euler #5
dividendo = 2520
residuo = 0
while residuo != (dividendo % 11) or residuo != (dividendo % 12) or residuo != (dividendo % 13) or residuo != (dividendo % 14) or residuo != (dividendo % 15) or residuo != (dividendo % 16) or residuo != (dividendo % 17) or residuo != (dividendo % 18) or residuo != (dividendo % 19) or residuo != (dividendo % 20):
    dividendo += 20
print(dividendo)