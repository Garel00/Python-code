#Problema 2 2019
#Regresar el segundo maximo elemento de un arreglo

#Valores test
data = [1, 20, -5, 345, -3, 2]

def get_Second_Max(data):
	first = float('-inf')
	second = float('-inf')
	
	for item in data:
		if item > first:
			second = first
			first = item
			
		elif item > second:
			second = item
	
	return second


print(get_Second_Max(data))
