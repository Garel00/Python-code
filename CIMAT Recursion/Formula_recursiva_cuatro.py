#Formula recursiva 4

memo = {}

def formula_cuatro(n):
	
	if n<=3:
		return 1
	
	if n >=4:
		if n in memo:
			return memo[n]
		
		memo[n] = formula_cuatro(n-1) + formula_cuatro(n-2) + formula_cuatro(n-3)
		return memo[n]
	

n = int(input("Ingresa el valor n: "))
print(formula_cuatro(n))
