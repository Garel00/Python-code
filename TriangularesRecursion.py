#Numeros triangulares recursion
lista_triangulares = []

def generador_triangulares(lista_triangulares,k):
	
	if k < 1:
		return 0
	
	if k == 1:
		lsta_triangulares.append(1)
		return 1
		
	triangular = k + generador_triangulares(lista_triangulares,k-1)
	
	lista_triangulares.append(triangular)
	return triangular


k = 6
print(generador_triangulares(lista_triangulares,k))
print(lista_triangulares)
