#Problema 3 2021

# =====================================================================
# FUNCIONES AUXILIARES PARA EL ÁLGEBRA DE POLINOMIOS (INCISO B)
# =====================================================================

def restar_listas(p1, p2):
    """Resta dos polinomios representados como listas de coeficientes."""
    max_len = max(len(p1), len(p2))
    resultado = [0] * max_len
    for i in range(max_len):
        v1 = p1[i] if i < len(p1) else 0
        v2 = p2[i] if i < len(p2) else 0
        resultado[i] = v1 - v2
    return resultado

def multiplicar_por_monomio_nativo(p, x_coef, constante):
    """
    Multiplica el polinomio P por (x_coef * x + constante).
    Para el algoritmo de Neville siempre es (1 * x - x_point), 
    así que x_coef siempre será 1.
    """
    # Al multiplicar por un término de grado 1, el grado aumenta en 1
    resultado = [0] * (len(p) + 1)
    for i in range(len(p)):
        # Multiplicación por el término independiente
        resultado[i] += p[i] * constante
        # Multiplicación por la 'x' (se desplaza una posición a la derecha)
        resultado[i + 1] += p[i] * x_coef
    return resultado

def dividir_por_escalar_nativo(p, escalar):
    """Divide todos los coeficientes del polinomio por un número real."""
    return [coef / escalar for coef in p]


# =====================================================================
# INCISO A: Evaluación numérica iterativa (Solo listas nativas)
# =====================================================================
def neville_evaluar_for(puntos, t):
    n = len(puntos)
    # Creamos una matriz de n x n llena de ceros usando listas de Python
    tabla = [[0.0] * n for _ in range(n)]
    
    # Caso base: Primera columna con los valores de 'y'
    for i in range(n):
        tabla[i][0] = puntos[i][1]
        
    # Construcción de la tabla columna por columna
    for j in range(1, n):
        for i in range(n - j):
            xi = puntos[i][0]
            xj = puntos[i + j][0]
            
            p_izq = tabla[i][j - 1]
            p_der = tabla[i + 1][j - 1]
            
            # Fórmula numérica de Neville
            tabla[i][j] = ((t - xj) * p_izq - (t - xi) * p_der) / (xi - xj)
            
    return tabla[0][n - 1]


# =====================================================================
# INCISO B: Construcción algebraica del polinomio (Solo listas nativas)
# =====================================================================
def neville_polinomio_for(puntos):
    n = len(puntos)
    # Matriz de n x n para guardar las listas de coeficientes
    tabla = [[None] * n for _ in range(n)]
    
    # Caso base: Polinomios constantes (Grado 0)
    for i in range(n):
        tabla[i][0] = [puntos[i][1]]
        
    # Construcción de polinomios de grados superiores
    for j in range(1, n):
        for i in range(n - j):
            xi = puntos[i][0]
            xj = puntos[i + j][0]
            
            p_izq = tabla[i][j - 1]
            p_der = tabla[i + 1][j - 1]
            
            # Multiplicamos algebraicamente por (x - xj) y (x - xi)
            termino_izq = multiplicar_por_monomio_nativo(p_izq, x_coef=1, constante=-xj)
            termino_der = multiplicar_por_monomio_nativo(p_der, x_coef=1, constante=-xi)
            
            # Numerador = termino_izq - termino_der
            numerador = restar_listas(termino_izq, termino_der)
            
            # Guardamos dividiendo el polinomio entre el escalar (xi - xj)
            tabla[i][j] = dividir_por_escalar_nativo(numerador, xi - xj)
            
    return tabla[0][n - 1]


# =====================================================================
# EJECUCIÓN DE PRUEBA (Ejemplo de la imagen)
# =====================================================================
if __name__ == "__main__":
    puntos_examen = [(0, 1), (1, 3)]
    t_examen = 2
    
    # Probar Inciso A
    res_a = neville_evaluar_for(puntos_examen, t_examen)
    print("=== RESULTADO INCISO A ===")
    print(f"Valor en t={t_examen}: {res_a}")
    
    # Probar Inciso B
    res_b = neville_polinomio_for(puntos_examen)
    print("\n=== RESULTADO INCISO B ===")
    print(f"Lista de coeficientes obtenida: {res_b}")
    print(f"Interpretación (de menor a mayor grado): {res_b[0]} + {res_b[1]}x")
