#Ajedrez2

memo = {}
posmenor = 100 # Nuestro "infinito" manual

def captura(posx, posy, a, b):
    # 1. Límites del tablero (Suponiendo 8x8)
    if posx < 0 or posx > 7 or posy < 0 or posy > 7:
        return 100
    
    # 2. Condición de éxito: Capturamos la pieza (llegamos a 0,0)
    if posx == 0 and posy == 0:
        return 0
    
    # 3. Revisar si ya pasamos por aquí
    if (posx, posy) in memo:
        return memo[(posx, posy)]
    
    # Marcamos como visitado con un valor alto para evitar ciclos
    memo[(posx, posy)] = 100

    # 4. Explorar movimientos (Usando tus saltos a y b)
    # Intentamos las 4 direcciones básicas con tus variables
    op1 = captura(posx + a, posy + b, a, b)
    op2 = captura(posx - a, posy - b, a, b)
    op3 = captura(posx - a, posy + b, a, b)
    op4 = captura(posx + a, posy - b, a, b)
    op5 = captura(posx+b, posy + a, a, b)
    op6 = captura(posx-b, posy +a, a, b)
    op7 = captura(posx +b, posy - a, a, b)
    op8 = captura(posx - b, posy -a, a, b)

    # 5. Buscar el menor de las opciones manualmente
    res_menor = op1
    if op2 < res_menor: res_menor = op2
    if op3 < res_menor: res_menor = op3
    if op4 < res_menor: res_menor = op4
    if op5 < res_menor: res_menor = op5
    if op6 < res_menor: res_menor = op6
    if op7 < res_menor: res_menor = op7
    if op8 < res_menor: res_menor = op8

    # Guardamos el resultado en el memo (1 movimiento actual + el resto)
    memo[(posx, posy)] = 1 + res_menor
    return memo[(posx, posy)]

# --- Valores Iniciales ---
init1, init2 = 0, 0   # Tu posición
end1, end2 = 7, 4     # Posición de la pieza a capturar

# posx y posy son la distancia relativa
posx = end1 - init1
posy = end2 - init2

a = 1  # Salto en x
b = 2  # Salto en y

resultado = captura(posx, posy, a, b)

if resultado >= 100:
    print("Not posible to eat the piece")
else:
    print("Movimientos:", resultado)
