#Problema 6 2025

def multiplos(lista):
	lista_b = []
	#Arreglo auxiliar historial
	historial = []
	for item in lista:
		lista_b.append(False)
	
	index = 0
	for item in lista:
		for itemh in historial:
			if item % itemh == 0:
				lista_b[index] = True
				break
		if not lista_b[index]:
			historial.append(lista[index])
		index += 1
				
		
	return lista_b
	
s = [5,3,15,2,7,14,28,4,6]

salida = multiplos(s)
print(salida)
