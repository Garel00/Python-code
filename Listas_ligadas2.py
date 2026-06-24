#Listas ligadas ejemplo

class Nodo:
    """Clase que representa un elemento individual dentro de la lista ligada."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Apunta a None por defecto hasta que se enlace


class ListaLigada:
    """Clase que maneja la estructura y operaciones de la lista ligada."""
    def __init__(self):
        self.cabeza = None  # La lista inicia vacía

    def insertar_inicio(self, dato):
        """Inserta un nuevo nodo al principio de la lista. Complejidad: O(1)"""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza  # Apunta a lo que antes era la cabeza
        self.cabeza = nuevo_nodo            # La nueva cabeza es el nodo recién creado

    def insertar_final(self, dato):
        """Inserta un nuevo nodo al final de la lista. Complejidad: O(n)"""
        nuevo_nodo = Nodo(dato)
        
        # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        
        # Si no está vacía, recorremos hasta el último nodo
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        
        # Enlazamos el último nodo con el nuevo
        actual.siguiente = nuevo_nodo

    def mostrar(self):
        """Recorre la lista e imprime su estructura de forma visual. Complejidad: O(n)"""
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> None")

    def buscar(self, clave):
        """Busca un valor en la lista. Retorna True si existe, False si no. Complejidad: O(n)"""
        actual = self.cabeza
        while actual:
            if actual.dato == clave:
                return True  # Elemento encontrado
            actual = actual.siguiente
        return False  # Se llegó al final y no se encontró

    def eliminar(self, clave):
        """Elimina la primera ocurrencia de un valor en la lista. Complejidad: O(n)"""
        actual = self.cabeza
        anterior = None

        # Caso 1: La lista está completamente vacía
        if not actual:
            return False

        # Caso 2: El elemento a eliminar está justo en la cabeza
        if actual.dato == clave:
            self.cabeza = actual.siguiente  # La cabeza ahora apunta al segundo nodo
            return True

        # Caso 3: El elemento está en medio o al final. Buscamos el nodo.
        while actual and actual.dato != clave:
            anterior = actual
            actual = actual.siguiente

        # Si el ciclo terminó y actual es None, significa que no encontramos el valor
        if not actual:
            return False

        # Si lo encontramos, "nos saltamos" el nodo actual reasignando el puntero del anterior
        anterior.siguiente = actual.siguiente
        return True

    def invertir(self):
        """Invierte el orden de la lista in-place (modificando punteros). Complejidad: O(n)"""
        anterior = None
        actual = self.cabeza
        
        while actual:
            siguiente_nodo = actual.siguiente  # 1. Guardamos temporalmente el resto de la lista
            actual.siguiente = anterior        # 2. Invertimos el sentido del puntero actual
            anterior = actual                  # 3. Avanzamos 'anterior' una posición
            actual = siguiente_nodo            # 4. Avanzamos 'actual' al siguiente nodo guardado
            
        self.cabeza = anterior  # Al final, 'anterior' queda apuntando a la nueva cabeza


# ==========================================
# Bloque de ejecución con el ejemplo propuesto
# ==========================================
if __name__ == "__main__":
    # 1. Inicializar la lista
    lista = ListaLigada()
    
    # 2. Insertar elementos
    lista.insertar_final(10)
    lista.insertar_final(20)
    lista.insertar_inicio(5)
    
    print("--- Estado Inicial ---")
    print("Lista original:")
    lista.mostrar()  # Esperado: 5 -> 10 -> 20 -> None
    
    # 3. Probar la búsqueda
    print("\n--- Probando Búsqueda ---")
    print("¿Está el número 10 en la lista?:", lista.buscar(10))  # Esperado: True
    print("¿Está el número 99 en la lista?:", lista.buscar(99))  # Esperado: False
    
    # 4. Probar la eliminación
    print("\n--- Probando Eliminación ---")
    lista.eliminar(10)
    print("Después de eliminar el 10:")
    lista.mostrar()  # Esperado: 5 -> 20 -> None
    
    # 5. Probar la inversión de la lista
    print("\n--- Probando Inversión ---")
    lista.invertir()
    print("Lista invertida:")
    lista.mostrar()  # Esperado: 20 -> 5 -> None
