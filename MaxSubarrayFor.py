#MaxCrossingSubarray

import math

def max_subarray(A, low, mid, high):
	
	#Parte cross, sumando parte izq y der que tienen mid
	#Parte Izquierda
	left_sum = float("-inf")
	suml = 0
	for i in range(mid, low-1, -1):
		suml += A[i]
		if suml > left_sum:
			left_sum = suml
			il = i
	
	#Parte dercha
	right_sum = float("-inf")
	sumr = 0
	for i in range(mid+1, high+1, 1):
		sumr += A[i]
		if sumr > right_sum:
			right_sum = sumr
			ir = i
	
	#Suma del cross
	cross_total = right_sum + left_sum
	
	
	#Ahora, unicamente la parte izquierda
	oleft_sum = float("-inf")
	
	for i in range(mid, low-1, -1):
		osuml = 0
		for j in range(i, low-1, -1):
			osuml += A[j]
			if osuml > oleft_sum:
				oleft_sum = osuml
				oli = i
				olj = j
	
	#Ahora, unicamente la parte derecha
	oright_sum = float("-inf")
	
	for i in range(mid, high+1, 1):
		osumr = 0
		for j in range(i, high+1, 1):
			osumr += A[j]
			if osumr > oright_sum:
				oright_sum = osumr
				ori = i
				orj = j
	
	
	if oleft_sum >= cross_total and oleft_sum >= oright_sum:
		total_mayor = oleft_sum
		inicio = olj
		final = oli
		
	if oright_sum >= cross_total and oright_sum >= oleft_sum:
		total_mayor = oright_sum
		inicio = ori
		final = orj
		
	if cross_total >= oright_sum and cross_total >= oleft_sum:
		total_mayor = cross_total
		inicio = il
		final = ir
	
	matriz_resultado = [inicio, final, total_mayor]
	return matriz_resultado
	

A = [2, 8, -3, 2, 7, 1, 7, 8]
n = len(A)

resultado = max_subarray(A, 0, n//2, n-1)
print(resultado)
