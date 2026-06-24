#Problema 1 2021

def calculadora_primos(N):
	
	#Creamos una lista con el caso base, el primer primo, aqui se irran agregando los primos
	lista_primos = [2]
	k = 3 #El siguiente numero por pronarse si es primo o no
	
	while True:
		#El numero es primo hasta que se demuestre lo contrario
		es_primo = True
		for item in lista_primos:
			#La teoria fundamental de la aritmetica nos dice que
			#cualquier numero no primo es divisible entre numeros primos
			if k % item == 0:
				#Con demostrarse una vez, se vuelve false y 
				#se hace break al codigo
				es_primo = False
				break
		
		if es_primo:
			lista_primos.append(k)
		#sumamos 1 para seguir con el siguiente numero
		k += 1
		if len(lista_primos) >= N:
			break
	
	return lista_primos




N = 5

print(calculadora_primos(N))
	
