#Problema 5 2024

Arreglo = [-4,-6, -2, 3, 0, 6]

def min_arreglo(A):
	
	menor_num = float('inf')
	#Caso 1: todos los valores son mayores o iguales a 0
	#De paso, hagamos una lisa
	if all(x >= 0 for x in A):
		menor_num = 'inf'
		for item in A:
			if item == 0:
				continue
			elif item < menor_num:
				menor_num = item
		subarreglo = menor_num
		
	else:
		#Fuerza bruta
		rango = len(A)
		subarreglo = []
		for i in range(0, rango):
			matriz_temporal = [A[i]]
			multiplo_temporal = A[i]
			if A[i] < menor_num:
				menor_num = A[i]
				subarreglo = matriz_temporal
			
			if A[i] == 0:
				continue
			for j in range(i, rango):
				if j == i:
					continue
				elif A[j] == 0:
					break
				else:
					matriz_temporal.append(A[j])
					multiplo_temporal = multiplo_temporal * A[j]
					if multiplo_temporal < menor_num:
						menor_num = multiplo_temporal
						subarreglo = matriz_temporal
		
		
	return subarreglo
	

print(min_arreglo(Arreglo))
