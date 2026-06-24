#Problema 4 2019

#valores test

A1 = ["H", "H", "H", "F", "H", "H", "F", "F"]
k1 = 1

def citas_posibles(A, k):
	largo = len(A)
	conteo = 0
	
	for i in range(0, largo):
		#Vamos a contar solo cuando los hombres hagan match
		#con F, si contamos los match de F con H duplicariamos
		#el conteo
		if A[i] == "F" or A[i] == "O":
			continue
		
		for m in range(i-k, i+k+1):
			if m == i or m >= largo or i <= 0 or A[m] == "O":
				continue
			if A[i] != A[m]:
				conteo += 1
				#Definimos F como O
				#para evitar un duplicado de citas
				A[m] = "O"
			
		
		
	
	return conteo

print(citas_posibles(A1, k1))


