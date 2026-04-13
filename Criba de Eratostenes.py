#Criba de Eratostenes

def eratostenes(max):
    #Creacion del set natural
    set_natural = set()
    for i in range(1, max+1):
        set_natural.add(i)
    
    #Calcular el n^2 > max
    n = 1
    while True:
        n += 1
        if n**2 > max:
            break
    #Crear lista natural menor al rango n
    lista_menor = []
    for j in range(2, n):
        lista_menor.append(j)
    lista_criba = []
    es_primo = True
    #Descartar los numeros no primos de la lista menor
    for numero in lista_menor:
        for l in range(2, numero):
            if numero == l:
                break
            if numero % l == 0:
                es_primo = False
                break
            es_primo = True
        if es_primo:
            lista_criba.append(numero)
    #Crear los multiplos de todos los numeros primeros menores al rango n
    lista_de_sets = []
    k = 0
    for crib in lista_criba:
        set_crib = set()
        for i in range(crib*2, max+1, crib):
            set_crib.add(i)
        lista_de_sets.append(set_crib)
    for setn in lista_de_sets:
        set_natural -= setn
    print(f'Los numeros primos son {set_natural}')

eratostenes(2000000)