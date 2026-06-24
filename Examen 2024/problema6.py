#Problema 6 2024
#Metodo: ventanas deslizantes

#Valores test:
a1 = [8, 20, 15, 17, 12]
s1 = 34
a2 = [8, 20, 15, 17, 12]
s2 = 200

def menor(a,s):
	#El resultado es invalido, hasta que se demuestre lo contrario
	resultado = -1
	longitud_a = len(a)
	
	#Analizamos el caso base, el elemento 1
	if a[0] > s:
		resultado = 1
	
	#Si la matriz solo tiene un elemento, no hay que buscar mas, el resultado
	#ya esta definido
	elif longitud_a == 1:
		return resultado
	
	
	else:
		#Definimos la cola y la cabeza inicial de nuestra ventana deslizante
		tail = 0
		head = 1
		suma = a[0] + a[1]
		items = 2
		#Usamos un while para no limitar nuestras operaciones a un rango
		while True:
			if head > longitud_a-1:
				break
			if suma > s:
				if resultado == -1 or items < resultado:
					resultado = items
				tail +=1
				items = items - 1
				if tail == head:
					suma = a[head]
					items = 1
				else:
					suma = suma - a[tail-1]
				
			else:
				head += 1
				if head  > longitud_a-1:
					break
				
				suma = suma + a[head]
				items += 1
				
			

					
	return resultado
	

print(menor(a2, s2))
