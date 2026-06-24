#Problema 2 2022

def submatriz(matriz):
	#creamos la variable de maxima suma
	max_s = float('-inf')
	#creamos la matrix maxima
	max_matrix = []
	mn = len(matriz)
	for m in range(0,mn):
		for n in range(0,mn):
			#Caso base, un elemento es la mayor suma
			if matriz[m][n] > max_s:
				max_s = matriz[m][n]
				max_matrix = matriz[m][n]
			
			i = m
			j = n
			while True:
				i += 1
				j += 1
				if i>mn or j>mn:
					break
				# Digamos que quieres recortar un subcuadrado de la matriz
				f_inicio, f_fin = n, j  # Filas de la 1 a la 2 (el final es exclusivo)
				c_inicio, c_fin = m, i  # Columnas de la 1 a la 2

				# Recortar de forma eficiente en una línea:
				submatriz = [fila[c_inicio:c_fin] for fila in matriz[f_inicio:f_fin]]
				new_suma = 0
				for fila in submatriz:
					for valor in fila:
						new_suma += valor
				if new_suma>max_s:
					max_s = new_suma
					max_matrix = submatriz
				
				if len(submatriz) == mn:
					break
					
	
	
	return max_matrix
	
	

A = [(1, -10, 3), (-1, 1, 4), (0, 2, 7)]
print(submatriz(A))
