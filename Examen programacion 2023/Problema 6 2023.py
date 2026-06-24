#Problema 6 2023
#Cambio de dinero

s = 7
denominaciones = [1,2,5,10]
n = len(denominaciones)
def cambio(denominaciones, i, s):
    if s == 0:
        return 1
    if s < 0 or i >= len(denominaciones):
        return 0
    

    return cambio(denominaciones, i, s - denominaciones[i]) + cambio(denominaciones, i+1, s)

print(cambio(denominaciones, 0, s))