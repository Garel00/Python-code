#Problema 2 2020
import math
#se requiere para redondear hacia arriba
def scroll(p1, p2, n, s):
	
	#El valor es negativo, a menos que se ejecute alguna condicion valida
	steps = -1
	
	#Se analizaran 3 posibles casos
	
	#Caso 1: Si p2 es mayor a p1
	#y este es multiplo del salto
	if p2 > p1 and (p2-p1) % s == 0:
		#el mejor caso, va directo
		steps = (p2-p1)/s
		
	#Caso 2: podemos ir en retoceso
	elif p1 > p2 and (p1-p2) % s == 0:
		steps = (p1-p2)/s
	
	#Caso 3: Podemos llegar al final de pagina, 
	#y el camino de regreso a p2 es multiplo, este rebote
	#debe ser mas corto
	elif (n-p2) % s == 0 and (math.ceil((n-p1)/s) + (n-p2)/s) <= (math.ceil((n-1)/s) + (p2-1)/s):
		#En este caso, podemos llegar al final
		#y luego regresar a p2
		steps = math.ceil((n-p1)/s)
		steps += (n-p2)/s
	
	#Caso 4: Regresamos al inicio (pagina 1)
	#y entonces el camino es multiplo
	elif (p2-1) % s == 0:
		steps = math.ceil((n-1)/s)
		steps += (p2-1)/s
	
	#Si ninguna condicion se ejecuto, el multiplo es invalido
	#y no se guardo ningun valor distinto a -1
	return steps

p1 = 9
p2 = 8
n = 10
s = 2

print(scroll(9,8,10,2))
