#Problema 2 2025
A = [-4, 2, -6, 8, -2, 4, 2, -10, 8]

def funcion(A, low, high):
    if len(A) == 1:
        return A
    
    return A + funcion(A)
