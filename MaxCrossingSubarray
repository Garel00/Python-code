#Max crossing subarray

import math

def find_max_crossing_subarray(A, low, mid, high):
    # Parte izquierda: desde mid hacia abajo hasta low
    left_sum = float('-inf')
    suma = 0
    max_left = mid
    
    # En Python, para ir de mid a low (incluyéndolo), usamos range(mid, low - 1, -1)
    for i in range(mid, low - 1, -1):
        suma = suma + A[i]
        if suma > left_sum:
            left_sum = suma
            max_left = i
            
    # Parte derecha: desde mid + 1 hasta high
    right_sum = float('-inf')
    suma = 0
    max_right = mid + 1
    
    # En Python, para llegar hasta high inclusive, usamos range(mid + 1, high + 1)
    for j in range(mid + 1, high + 1):
        suma = suma + A[j]
        if suma > right_sum:
            right_sum = suma
            max_right = j
            
    # Retorna una tupla con (índice_inicio, índice_fin, suma_total)
    return (max_left, max_right, left_sum + right_sum)

# Ejemplo de uso:
mi_arreglo = [2, -3, 4, 5, -2, 3, -1]
n = len(mi_arreglo)
# En este ejemplo, mid sería el índice central
resultado = find_max_crossing_subarray(mi_arreglo, 0, (n-1)//2, n-1)

print(f"Amo y señor, el resultado es: {resultado}")
