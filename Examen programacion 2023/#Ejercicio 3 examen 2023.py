#Ejercicio 3 examen 2023
import time

def mi_rand():
    t = time.time()
    numero_aleatorio = t % 1
    # Redondeamos a 2 decimales
    return round(numero_aleatorio, 2)

# Prueba
print(mi_rand())

def arreglo(N):
    A = []
    for i in range(N):
        pi = []
        cuadrante = mi_rand()
        if cuadrante > 0.5:
            xi = 2 + 2*(mi_rand())
        else:
            xi = -2 -2*(mi_rand())

        cuadrante = mi_rand()
        if cuadrante > 0.5:
            yi = 2 + 2*(mi_rand())
        else:
            yi = -2 -2*(mi_rand())
        pi.append(xi)
        pi.append(yi)
        A.append(pi)
    return A

print(arreglo(3))
    
#Respuesta a la pregunta 2: se puede modificar el programa para que genere 360 puntos alrededor del circulo,
#sumar la distancia entre los puntos, esto aproximaria el valor de pi
#Nota: el randomizador en este ejercicio no sirve, python hace los calculos en unos cuantos nanosegundos