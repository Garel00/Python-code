#Probema 4 2022

sl = "TATATOTA"
sc = "TA"

def ocurrencia(sl, sc):
	#Calculamos la longitud de sc y sl
	corta = len(sc)
	larga = len(sl)
	s_inicio = 0
	s_fin = corta
	cantidad = 0
	rango_suma = larga - corta
	
	#Caso nulo
	if corta > larga:
		cantidad = "caso nulo"

	else:
		for _ in range((rango_suma+1)):
		
			if sc == sl[s_inicio:s_fin]:
				cantidad += 1
			
			s_inicio += 1
			s_fin += 1
	
	return cantidad


print(ocurrencia(sl, sc))
	
