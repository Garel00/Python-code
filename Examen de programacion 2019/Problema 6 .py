#Problema 6 2019

#valores test
N = 3
val_x = [0, 1, 2]
val_y = [0, 2, 0]

#Decidi crear una funcion para replicar las funciones de la recta:

def recta(m, x, xo, yo):
	y = m*x - m*xo + yo
	
	return y

def polygon_test(n, val_x, val_y, point_x, point_y):
	#definimos la variable es valido, 
	#esta sera True hasta que se demuestre lo contrario,
	es_valido = True

	#Para resolver este problema particular, se ve que ya estan ordenadas los vertices
	#de derecha a izquierda, si quisieramos hacerlo para puntos desordenados
	#podemos usar un diccionario, ordenarlo y luego sacar variables ordenadas
	
	#Creamos una lista de pendientes para usar en las funciones de la recta
	m_lista = []
	#Calculemos todas las pendientes:
	for i in range(n):
		#calculamos la pendiente del ultimo vertice
		#respecto al primer vertice
		if i == n-1:
			M = (point_y[i] - point_y[0])/(point_x[i] - point_x[0])
			m_lista.append(M)
		
		else:
			M = (point_y[i+1] - point_y[i])/(point_x[i+1] - point_x[i])
			
	
	#Primera validacion, si point_x esta en el rango
	if point_x < val_x[0] or point_x > val_x[N-1]:
		es_valido = False
	
	#Ahora, si paso la primer validacion, vamos con la siguiente para y
	if es_valido == True:
		#Primero, hay que determinar en que rango de x esta
		for p in range(n-1):
			if point_x > val_x[p] and point_x < val_x[p+1]:
				#El rango sera este!
				rango = p
			
			#ya conociendo el rango, hay que evaluar si cumple en las y...
		#calculemos pues el valor y maximo
		ymax = recta(m_lista[rango], point_x, val_x[rango], val_y[rango]
		if val_y > ymax:
			es_valido = False
		
		#ahora, hay que validar si el valor es mayor al
		#ultimo valor de y
		if val_y < val_y[n-1]:
			es_valido = False
		
	
	
	
	
	
	return es_valido
