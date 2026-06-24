#Problema 12 Euler project

def criba(n):
    #Generamos la lista vacia
    lista_primos = []
    #Todos los numeros son primos hasta que se demuestre lo contrario
    lista_primos = [True]*(n+1)
    # 0 y 1 no son primos
    lista_primos[0] = False
    lista_primos[1] = False
    for j in range(2,int(n**(1/2))+1):
        if lista_primos[j]:
            for k in range(j*j, n+1, j):
                lista_primos[k] = False
    primos = []
    for m in range(len(lista_primos)):
        if lista_primos[m]:
            primos.append(m)
    return primos

lista_primos = criba(100000)

def generador_triangulares(s):
    triangular = s*(s+1)/2
    return triangular

triangle_count = 800
while True:
    triangle_count += 1
    triangle = generador_triangulares(triangle_count)
    divisores = 1
    for primo in lista_primos:
        if primo >= int((triangle+1)/2):
            break
        triangle2 = triangle
        exp = 0
        while True:
            if triangle2 % primo == 0:
                triangle2 = triangle2 / primo
                exp += 1
            if triangle2 % primo != 0:
                divisores = divisores * (exp + 1)
                break
    if divisores >= 500:
        print(f"{triangle} is the first number with 500 divisors")
        break





