#Problema 1 2024 corregido
#Producto Kronecker

#valores test

A = [[1, 2], [3, 4]]
B = [[0, 5], [6, 7]]

def kronecker(A,B):
	
	matrix_k = []
	#Calculamos la longitud de las variables

	m = len(A)
	n = len(A[0])
	p = len(B)
	q = len(B[0])
	
	#Creamos la matriz de mp x nq
	mp = m*p
	nq = n*q
	
	for _ in range(mp):
		matrix_k.append([])
	
	for file in matrix_k:
		for _ in range(nq):
			file.append(0)
	
	for i in range(m):
		for j in range(n):
			for k in range(p):
				for l in range(q):
					matrix_k[i*m+k][j*n+l] = A[i][j]*B[k][l]
					
			
	
	
				
				
			
		
	return matrix_k

print(kronecker(A,B))
