#Ejercicio 2 programacion cimat 2023

#Primer funcion, multiplica un vector nx1 por una matriz nxn, el resultado sera un vector nx1
def multiplicar_matrices(x, matriz):
    posicion = 0
    matriz_resultado = []
    for value in x:
        multiplo = 0
        for number in matriz[posicion]:
            multiplo += value*number
        posicion += 1
        matriz_resultado.append(multiplo)
    return matriz_resultado

#Segunda funcion, multiplicar el producto por la traspuesta
def multiplicar_vectores(x, v):
    resultado = 0
    for value in v:
        for number in x:
            resultado *= number*value
    return resultado


matriz = [(1, 3), (2,4)]
x =  [-1,1]

primer_producto = multiplicar_matrices(x, matriz)
print(primer_producto)
print(multiplicar_vectores(x, primer_producto))