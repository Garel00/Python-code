#Problema 2 2021

def comparador_matrices(matrizA,matrizB):
	
	#La matriz no es inversa hasta que se demuestre lo contrario
	es_inversa = False
	
	#Paso 1: crear la matriz identidad de nxn
	mn = len(matrizA)
	matrizI = []
	for _ in range(mn):
		matrizI.append([])
	for m in range(mn):
		for n in range(mn):
			if m == n:
				matrizI[m].append(1)
			else:
				matrizI[m].append(0)
	
	#Ahora, toca calcular la multiplicacion
	#Creamos la matriz multiplicacion
	matrizm = []
	for _ in range(mn):
		matrizm.append([])
	
	for m in range(mn):
		for n in range(mn):
			matrizm[m].append(0)
		

	for i in range(mn):
		for j in range(mn):
			suma = 0
			for k in range(mn):
				suma += matrizA[i][k]*matrizB[k][j]
			matrizm[i][j] = suma
			
		
	if matrizm == matrizI:
		es_inversa = True
	
	return es_inversa


matrizA = [(1,-2), (-3,5)]
matrizB = [(-5,-2), (-3,-1)]

print(comparador_matrices(matrizA,matrizB))

