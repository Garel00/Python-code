#Problema 5

#Valores test
x = 0.1
n = 2

def taylor_sin(x,n):
	up = 1
	down = 1
	sign = -1
	resultado = 0
	for i in range(1, n+1):
		#Calculamos el menor numero
		#de multiplicaciones
		if i == 1:
			up = x
		else:
			up = up * (x**2)
		
		#Para el factorial
		if i == 1:
			pre_factorial = 1
		else:
			valor = (2*i-1)
			valor2 = (2*i-2)
			#Aqui solo hay que calcular la multiplicacion
			#del valor 2n-1 y 2n-2, y multiplicarlo por el factorial anterior
			#esto nos da como resultado el valor del factorial actual
			pre_factorial = valor * valor2
			
		down = pre_factorial * down
		sign = -sign
		resultado += sign*up/down
	
	return resultado
