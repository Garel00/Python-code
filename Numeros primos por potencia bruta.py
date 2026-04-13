## Numeros primos por potencia bruta
def es_primo(n):
    # Los números menores o iguales a 1 no son primos
    if n <= 1:
        return False
    
    # Fuerza bruta: probamos todos los números desde 2 hasta n-1
    for i in range(2, n):
        if n % i == 0:
            # Si el residuo es 0, encontramos un divisor; no es primo
            return False
            
    return True

# --- Prueba del programa ---
limite = 2000000
print(f"Números primos hasta el {limite}:")

for num in range(1, limite + 1):
    if es_primo(num):
        print(num, end=" ")