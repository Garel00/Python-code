#Suma de todos los n cuadrados

def sumatoria_cuadrados(n):
    if n == 1:
        return 1
    return n**2 + sumatoria_cuadrados(n-1)

print(sumatoria_cuadrados(4))
