#Generar sort list
A = [2,3,4,1,7,5]

def sorteo(lista):
    for i in range(1, len(lista)):
        key = A[i]
        j = i-1
        while j >= 0 and key > A[j]:
            A[j+1] = A[j]
            j = j-1

        A[j+1] = key
    return lista


sorteado = sorteo(A)
print(sorteado)


