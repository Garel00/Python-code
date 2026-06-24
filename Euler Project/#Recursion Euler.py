#Recursion Euler
# Un diccionario para recordar rutas ya calculadas
memoria = {}

def contar_rutas(x, y):
    # Creamos una llave única para las coordenadas
    posicion = (x, y)
    
    # --- PASO DE ORO: Si ya lo calculamos, lo devolvemos ---
    if posicion in memoria:
        return memoria[posicion]
    
    # 1. Casos base (Si llegas al borde de la cuadrícula 20x20)
    if x == 0 or y == 0:
        return 1
    
    # 2. Paso recursivo con "Memoria"
    # Guardamos el resultado en el diccionario antes de retornarlo
    memoria[posicion] = contar_rutas(x - 1, y) + contar_rutas(x, y - 1)
    
    return memoria[posicion]

print(contar_rutas(20, 20))