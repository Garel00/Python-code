#Pagos

def pago(monto, billetes, i):
	
	if monto == 0:
		return 1
	
	if monto < 0 or i == len(billetes):
		return 0
	
		
	return pago(monto-billetes[i], billetes, i) + pago(monto, billetes, i+1)
	

monto = 100

monedas = [5, 10, 20, 50]

print(pago(monto, monedas, 0))
		
