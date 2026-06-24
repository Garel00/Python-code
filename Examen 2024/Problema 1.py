#Problema 1 2024
#Producto Kronecker

#valores test

A = [[1, 2], [3, 4]]
B = [[0, 5], [6, 7]]

def kronecker(A,B):
	
	matrix_k = []
	longitud_B = len(B)
	contador = 0
	
	for fileA in A:
		for itemA in fileA:
			for fileB in B:
				submatrix = []
				for itemB in fileB:
					submatrix.append(itemA*itemB)
					
				matrix_k.append(submatrix)
						
	return matrix_k

print(kronecker(A,B))
