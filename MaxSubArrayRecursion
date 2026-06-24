# MaxCrossingSubarray usando recursión (Divide y vencerás)

def max_crossing_subarray(A, low, mid, high):

    # Parte izquierda
    left_sum = float("-inf")
    suma = 0
    max_left = mid

    for i in range(mid, low - 1, -1):
        suma += A[i]
        if suma > left_sum:
            left_sum = suma
            max_left = i

    # Parte derecha
    right_sum = float("-inf")
    suma = 0
    max_right = mid + 1

    for j in range(mid + 1, high + 1):
        suma += A[j]
        if suma > right_sum:
            right_sum = suma
            max_right = j

    return [max_left, max_right, left_sum + right_sum]


def max_subarray_recursive(A, low, high):

    # Caso base: un solo elemento
    if low == high:
        return [low, high, A[low]]

    # División del arreglo
    mid = (low + high) // 2

    # Recursión izquierda
    left_result = max_subarray_recursive(A, low, mid)

    # Recursión derecha
    right_result = max_subarray_recursive(A, mid + 1, high)

    # Subarreglo cruzando el medio
    cross_result = max_crossing_subarray(A, low, mid, high)

    # Comparar resultados
    if (left_result[2] >= right_result[2] and
        left_result[2] >= cross_result[2]):
        return left_result

    elif (right_result[2] >= left_result[2] and
          right_result[2] >= cross_result[2]):
        return right_result

    else:
        return cross_result


# Programa principal
A = [2, 8, -3, 2, 7, 1, 7, 8]

resultado = max_subarray_recursive(A, 0, len(A) - 1)

print("Inicio:", resultado[0])
print("Final:", resultado[1])
print("Suma máxima:", resultado[2])
