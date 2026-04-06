#Project Euler problema 6
suma_natural = 0
suma_cuadrado = 0

for natural in range(1,101):
    suma_natural += natural
suma_natural = suma_natural**2
print(f"La suma de los numeros naturales del 1 al 100 elevada al cuadrado es {suma_natural}")

for cuadrado in range(1,101):
    suma_cuadrado += cuadrado**2
print(f"La suma de los numeros al cuadrado en el rango de 1 a 100 es {suma_natural}")

diferencia = suma_natural - suma_cuadrado
print(f"La diferencia de las sumas al cuadrado es {diferencia}")
