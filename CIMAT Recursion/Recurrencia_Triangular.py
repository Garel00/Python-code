#Recurrencia triangular

def F(n):
	
	if n == 0:
		return 0
	
	if n == 1:
		return 1
	
	if n == 2:
		return 3
	
	return 3*F(n-1) - 3*F(n-2) + F(n-3)
	
n = int(input("Ingresa el valor n: "))
print(F(n))
