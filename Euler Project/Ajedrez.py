#CapturarPieza

memo = {}
def captura(posx, posy, a, b, conteo=0):
	
	if posx % a != 0 and (posx-b) % a != 0:
		print("Not posible to eat the piece")
		
	if posy % b != 0 and (posy-a) % b != 0:
		print("Not posible to eat the piece")
	
	if posx == 0 and posy == 0:
		return 1
	
	if posx < 0 and posy < 0:
		return 0
	
	if (posx, posy, a, b) in memo:
		return memo
	
	if a+b < posmenor and posx == 0 and posy == 0:
		posmenor = a + b
		amenor = a
		bmenor = b
		
	memo[(posx, posy, a, b)] = (captura(posx-a, posy, a, b) + captura(posx, posy-b, a, b)
	+ captura(posx-a, posy-b, a, b) + captura(posx-b, posy, a, b) + captura(posx, posy-a, a, b)
	+ captura(posx+a, posy, a, b) + captura(posx, posy+b, a, b)
	+ captura(posx+a, posy+b, a, b) + captura(posx+b, posy, a, b) + captura(posx, posy+a, a, b))
	return memo
	


init1 = 0
init2 = 0

end1 = 0
end2 = 0

posx = abs(end1 - init1)
posy = abs(end2 - init2)
posmenor = float("inf")
amenor = 0
bmenor = 0

a = 0
b = 0

print(captura(posx, posy, a, b))
