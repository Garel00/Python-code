# Problema 3 examen 2025


def push(numero, lista):
	
	n = len(lista)
	#Caso base: la lista esta vacia
	if not lista:
		lista.append(numero)
		return lista
	
	for i in range(n):
		if numero < lista[i]:
			for j in range(i, n):
				key = lista[j]
				lista[j] = numero
				numero = key
			lista.append(numero)
			return lista
		
	lista.append(numero)
		
	return lista
	

lista = []
lista = push(0, lista)
lista = push(4, lista)
lista = push(2, lista)
lista = push(3, lista)
print(lista)
