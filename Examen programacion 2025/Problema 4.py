#Problema 4 examen 2025

def ApproximateIntegral(x1, x2, f, N):
	#Simulemos que la funcion es x cuadrada para el test
	a = x2 - x1
	
	#Para calcular b, aproximemos usando el maximo
	#valor encontrado en una evaluacion de 1000 pts de la funcion
	b = 0
	for i in range(1000):
		xe = (i/1000)*a + x1
		y = f(xe)
		if y > b:
			b = y
			
	A = a*b
	Ncruz = 0
	Npunto = 0
	
	for _ in range(N+1):
		
		#Multiplicamos por x2 para que sea un valor
		#proporcional dentro del rango
		xr = a*rand01() + x1
		
		#Ahora para y
		yr = b*rand01()
		
		#Como xr se genera en el dominio, este siempre existira
		
		#por otra parte, validamos que exista en y
		fx = f(xr)
		
		if yr > fx:
			Npunto += 1
		
		else:
			Ncruz += 1
	
	I = A * Ncruz / (Npunto+Ncruz)
	
	return I
		
		
	
	
		
		
	
	
	
	return 0

def f(x):
	return x**2
#Supongamos fx = x**2

x1 = 0
x2 = 7
a = x2 - x1
N = 500

print(ApproximateIntegral(x1, x2, f, N)

