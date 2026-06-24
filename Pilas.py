#Problema de pilas
pila = ["(","(",")","{","(",")","(",")","}","{","}"]

def comprobante(pila):
	comprobador = []
	n = len(pila)
	#Diccionario para mapear
	mapeo = {')':'(', '}':'{'}
	
	for item in pila:
		if item in ['(', '{']:
			comprodabor.append(item)
		else:
			if not comprobador or comprobador.pop() != mapeo[item]:
				return False
	
	return len(pila) == 0

		
		
