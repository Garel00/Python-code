#Héctor Eduardo Garcia Elizarraraz
#Tarea 1: Problema 1
#Para calcular an cuando n cuando tiende a infinito
#debemos utilizar un valor muy grande...
#con recursion no es efectivo el algoritmo, nos quedaria exponencial,
#un proceso iterativo queda con tamaño On

#Proponemos n = 2000
n_max = 40

#Ponemos los valores iniciales
an_menos2 = 0
an_menos1 = 1

#Creamos un metodo en el que nos dice el valor de n respecto a la aporximacion:
aproximaciones = []
for n in range(2, n_max+1):
	an = 4*an_menos1 + 3*an_menos2
	aproximacion = (an/an_menos1) - 2
	aproximaciones.append(aproximacion)
	print(f"El valor de la aproximacion cuando n= {n} es igual a: {aproximacion}")
	an_menos2 = an_menos1
	an_menos1 = an

#calculemos tambien la raiz de 7 de forma directa
raiz_7 = 7**(1/2)

print(f"El valor del calculo directo es: {raiz_7}")
