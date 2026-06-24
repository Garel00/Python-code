#Problema 4 2024

# ==========================================
# 1. DEFINICIÓN DEL NODO (EL MOLDE CON CLASES)
# ==========================================
class Node:
    def __init__(self, valor):
        self.dato = valor   # Guarda el número/dato
        self.sig = None     # Guarda la referencia al siguiente nodo (empieza en None)


# ==========================================
# 2. FUNCIÓN DE INVERSIÓN (IGUAL A C++)
# ==========================================
def invierte_con_clases(head):
    actual = head
    prev = None
    sig = None

    while actual is not None:
        # A) Guarda el siguiente nodo para no perder la lista
        sig = actual.sig
        
        # B) Invierte la flecha: el actual ahora apunta hacia atrás (a prev)
        actual.sig = prev
        
        # C) Mueve ambos apuntadores un paso hacia adelante
        prev = actual
        actual = sig

    # Cuando 'actual' llega a None, 'prev' se queda parado en el último nodo,
    # el cual se convierte en la nueva cabeza de la lista invertida.
    return prev


# ==========================================
# 3. FUNCIÓN AUXILIAR PARA IMPRIMIR LA LISTA
# ==========================================
def imprimir_lista(head):
    actual = head
    while actual is not None:
        print(actual.dato, end=" → ")
        actual = actual.sig
    print("NULL")


# ==========================================
# 4. CREACIÓN DE LA ENTRADA (EJEMPLO DEL EXAMEN)
# ==========================================
# Creamos los 9 nodos de forma independiente usando el molde
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

# Conectamos las flechas (.sig) de izquierda a derecha: 1 -> 2 -> ... -> 9 -> NULL
n1.sig = n2
n2.sig = n3
n3.sig = n4
n4.sig = n5
n5.sig = n6
n6.sig = n7
n7.sig = n8
n8.sig = n9  # El n9 ya apunta a None por defecto desde el molde


# ==========================================
# 5. DEMOSTRACIÓN EN CONSOLA
# ==========================================

# Imprimimos el estado inicial
print("Lista original L:")
imprimir_lista(n1)

print("-" * 45)

# Invertimos la lista pasándole la cabeza original (n1)
nueva_cabeza = invierte_con_clases(n1)

# Imprimimos el resultado final
print("Lista invertida L':")
imprimir_lista(nueva_cabeza)

