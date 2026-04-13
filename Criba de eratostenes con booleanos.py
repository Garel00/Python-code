## Criba de eratostenes con booleanos, optimizada

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

print(criba(200))


