# Irracionales con recursion
# Numero de iteraciones n
n_max = 25

def irracional_recursion(n):
    if n <= 0:
        an = 0
        return an
    if n == 1:
        an = 1
        return an
    else:
        an = 4 * irracional_recursion(n - 1) + irracional_recursion(n - 2)
        return an

# Calculamos el valor final llamando a la función
an_final = irracional_recursion(n_max)
an_anterior = irracional_recursion(n_max - 1)

# Calculamos la aproximacion fuera de la recursión para obtener el resultado final
aproximacion = (an_final / an_anterior) - 2

print(f"El valor de la posicion {n_max} es igual a {aproximacion}")

# Calculemos tambien la raiz de 7 de forma directa
raiz_7 = 7**(1/2)

print(f"El valor del calculo directo es: {raiz_7}")
