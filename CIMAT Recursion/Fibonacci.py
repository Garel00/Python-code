#Fibonacci Recursivo
k = 0
def fibonacci(n):
	global k
	k += 1
	
	if n <= 0:
		return 0
	
	if n == 1:
		return 1
	
	return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Ingresa el valor n: "))
print(fibonacci(n))
print(f"Llamadas recursivas {k}")

#En realidad, la sucesion de fibonacci es la siguiente:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
#no pude agregar los saltos a como los pedia la pagina omegaup
