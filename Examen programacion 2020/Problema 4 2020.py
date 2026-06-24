#Problema 4 examen 2020
lista_triangulares = []
def comprobar_triangular(k):
	n = 1
	triangular = 0
	
	#El resultado es falso hasta que se demuestre lo contrario
	resultado = False
	while True:
		triangular = n+triangular
		
		if k == triangular:
			resultado = True
			break
		
		if triangular > k:
			break
		n+= 1
	
	
	return resultado




k = 6
print(comprobar_triangular(k))
