#Examen 1 2019

#Valores test
N = 12345

def Invertir_Num(N):
	
	base = 1
	inverso = 0
	k = 0
	
	while True:
		k = N // base
		if k <= 1:
			break
		else:
			base = base * 10
	
	base2 = 1
	
	while base >= 1:
		valor = N // base
		inverso += valor * base2
		N = N - (valor*base)
		base2 = base2 * 10
		base = base / 10
	
	inverso = int(inverso)
	return inverso

print(Invertir_Num(N))
