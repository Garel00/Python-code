#Problema 3 2019
#Rotar matriz

#Valores test
I = [[10, 50, 70, 0], [200, 200, 170, 200], [0, 45, 120, 156], [2, 78, 89, 20]]

def rotar_matriz(I):
	m = len(I)
	matriz_r = []
	
	#Creamos una matriz con valores 0 para defninir las posiciones
	for _ in range(m):
		matriz_r.append([])
	
	for fila in matriz_r:
		for _ in range(m):
			fila.append(0)
	
	k = 0
	for i in range(m-1, -1, -1):
		
		for j in range(m):
			matriz_r[j][k] = I[i][j]
		
		k += 1
			
		
	
	return matriz_r
	

print(rotar_matriz(I))
