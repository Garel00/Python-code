#Problema 3 2020

def longitud(n, k):
	divisor = 1
	
	if k == 0:
		k = 1
	
	else:
		k = k*10
	
	while True:
		division = n//divisor
		
		if division <= 0:
			break
		else:
			divisor = divisor * 10
	
	while True:
		if divisor == k:
			resultado = n//divisor
			break
			
		n = n - (n//divisor)*divisor
		divisor = divisor/10
		
	return resultado
	

n = 53678
k = 1

print(longitud(n,k))
