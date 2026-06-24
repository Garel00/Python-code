#Problema 1 2025 metodo pro

def det22(matriz):
    det = matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
    return det

def det33(matriz):
    total = 0
    for c in range(3):
        submatriz = [[matriz[i][j] for j in range(3) if j != c] for i in range(1, 3)]
        if c % 2 == 0:
            signo = 1
        else:
            signo = -1
        total += matriz[0][c] * signo * det22(submatriz)
    return total

def det44(matriz):
    total = 0
    for c in range(4):
        submatriz = [[matriz[i][j] for j in range(4) if j !=c] for i in range(1, 4)]
        if c % 2 == 0:
            signo = 1
        else:
            signo = -1
        total += matriz[0][c] * signo * det33(submatriz)
    return total



matriz4 = [(1,2,3,4), (5,7,7,8), (9,10,18,12), (13,14,15,16)]

print(det44(matriz4))