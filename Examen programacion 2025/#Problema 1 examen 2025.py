#Problema 1 examen 2025


def determinante3(matriz):
    cofactor1 = matriz[0][0]
    cofactor2 = matriz[0][1]
    cofactor3 = matriz[0][2]
    a1 = cofactor1*((matriz[1][1]*matriz[2][2])-(matriz[1][2]*matriz[2][1]))
    a2 = cofactor2*((matriz[1][0]*matriz[2][2])-(matriz[1][2]*matriz[2][0]))
    a3 = cofactor3*((matriz[1][0]*matriz[2][1])-(matriz[1][1]*matriz[2][0]))
    determinante3 = a1 - a2 + a3
    return determinante3


def determinante4(matriz):
    cofactor1 = matriz[0][0]
    cofactor2 = matriz[0][1]
    cofactor3 = matriz[0][2]
    cofactor4 = matriz[0][3]

    matriz1 = [list(fila) for fila in matriz]
    matriz1.pop(0)
    for fila in matriz1:
        fila.pop(0)
    
    matriz2 = [list(fila) for fila in matriz]
    matriz2.pop(0)
    for fila in matriz2:
        fila.pop(1)
    
    matriz3 = [list(fila) for fila in matriz]
    matriz3.pop(0)
    for fila in matriz3:
        fila.pop(2)
    
    matriz4 = [list(fila) for fila in matriz]
    matriz4.pop(0)
    for fila in matriz4:
        fila.pop(3)
    
    determinante4 = cofactor1*determinante3(matriz1) - cofactor2*determinante3(matriz2) + cofactor3*determinante3(matriz3) - cofactor4*determinante3(matriz4)
    return determinante4

matriz3 = [(1,2,3), (4,5,6), (7,8,9)]
matriz4 = [(1,2,3,4), (5,7,7,8), (9,10,18,12), (13,14,15,16)]
print(matriz4)

resultado4 = determinante4(matriz4)
print(resultado4)