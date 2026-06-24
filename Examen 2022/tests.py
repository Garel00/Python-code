#tests

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Digamos que quieres recortar un subcuadrado de la matriz
f_inicio, f_fin = 1, 3  # Filas de la 1 a la 2 (el final es exclusivo)
c_inicio, c_fin = 1, 3  # Columnas de la 1 a la 2

# Recortar de forma eficiente en una línea:
submatriz = [fila[c_inicio:c_fin] for fila in matriz[f_inicio:f_fin]]

