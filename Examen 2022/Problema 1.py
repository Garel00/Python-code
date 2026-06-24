#Problema 1 Examen 2022

def mediana(list):
	ordered_list = []
	mediana = 0
	for item in list:
		if len(ordered_list) == 0:
			ordered_list.append(item)
		elif item >= ordered_list[-1]:
			ordered_list.append(item)
		else: #Here the ordered_list[i] is < than the item
			value = item
			n = len(ordered_list)
			for k in range(n):
				key = ordered_list[k]
				if value < key:
					ordered_list[k] = value
					value = key
			ordered_list.append(value)
	
	l = len(ordered_list)
	if l % 2 == 0:
		s = l//2
		mediana = (ordered_list[s] + ordered_list[s-1])/2
	else:
		s = l//2
		mediana = (ordered_list[s-1])
		
				
	
	
	return mediana

lista = [-2, 10, 1, 3, 4, 6]

print(mediana(lista))
