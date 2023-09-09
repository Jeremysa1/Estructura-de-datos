class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None

    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def pop(self, dato_a_quitar):
        if self.tope is None:
            return
        if self.tope.dato == dato_a_quitar:
            self.tope = self.tope.siguiente
        else:
            actual = self.tope
            while actual.siguiente and actual.siguiente.dato != dato_a_quitar:
                actual = actual.siguiente
            if actual.siguiente:
                actual.siguiente = actual.siguiente.siguiente

    def mostrar_pila(self):
        actual = self.tope
        while actual:
            print(actual.dato)
            actual = actual.siguiente


pila = Pila()

pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4)

elemento_a_quitar = 3

pila.pop(elemento_a_quitar)

pila.mostrar_pila()