#Problema 5 2022
#Colesky

A = [
    [4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98]
]

def colesky(A):
	
	n = len(A)
	matriz_l = []
	
	#Creamos una matriz vacia con puros ceros
	#para tener ubicaciones definidas, posteriormente
	#se le asignaran valores, al tener un 0 predefinido
	#evitamos un out of range y podemos posicionar los 
	#lij en el lugar preciso desde el inicio
	for _ in range(n):
		matriz_l.append([])
	
	for fila in matriz_l:
		for _ in range(n):
			fila.append(0)
			
	
	#Para la sumatoria de las lij, es necesario un ciclo doble for anidado
	for j in range(n):
		
		sumatoria_ljj = 0
		for k in range(0, j):
			sumatoria_ljj += (matriz_l[j][k])**2
		
		for i in range(n):
				
			if i == j:
				matriz_l[i][j] = (A[i][j] - sumatoria_ljj)**(1/2)
				
			elif j > i:
				continue
	
			else:
				sumatoria_lij = 0
				for k in range(0, j):
					sumatoria_lij += (matriz_l[i][k])*(matriz_l[j][k])
				matriz_l[i][j] = (A[i][j] - sumatoria_lij)/matriz_l[j][j]
				
		
			
	
	return matriz_l

print(colesky(A))
	
