#Problema 5 2025

def contar(lista):
	maximo = 0
	for item in lista:
		if item > maximo:
			maximo = item
	
	salida = []
	for _ in range(maximo+1):
		salida.append(0)
	
	for value in lista:
		salida[value] += 1
	
		
	
	return salida

entrada = [8,3,4,2,1,3,2,7]

salida = contar(entrada)
print(salida)
