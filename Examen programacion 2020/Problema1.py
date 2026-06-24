#Problema 1 2020


def bool_cover(a, b, v):
	
	
	#La longitud de a = longitud de b
	#esta longitud nos servira para los indices
	n = len(a)
	
	#Creamos una lista respuesta
	lista_respuesta = []
	
	#Todos los valores son falsos hasta que
	#se demuestre lo contrario
	for _ in range(n):
		lista_respuesta.append(False)
		
	#accedemos a cada item de v
	for item in v:
		#Agregamos 1 contador para el indice
		i = 0
		for _ in range(n):
			if item >= a[i] and b[i] >= item:
				lista_respuesta[i] = True
			
			i += 1
	#La respuesta es verdadera hasta que se
	#demuestre lo contrario
	booleano = True
	
	for item in lista_respuesta:
		if not item:
			booleano = False
			break
		
	
	return booleano
	

a = [3,2,8]
b = [4,5,9]
v = [3,8]

print(bool_cover(a,b,v))
