from .tipos import Item

class Nodo:
    def __init__(self, valor: Item, mensaje_id: int):
        self.valor = valor
        self.mensaje_id = mensaje_id
        self.siguiente = None

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.contador_id = 1

    def esta_vacia(self):
        return self.primero is None

    def encolar(self, valor: Item):
        nuevo_nodo = Nodo(valor, self.contador_id)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo
        self.contador_id += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.primero.valor
        mensaje_id = self.primero.mensaje_id
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        return {"mensaje_id": mensaje_id, "valor": valor}

    def ver_listado(self):
        contenido = []
        nodo_actual = self.primero
        while nodo_actual:
            contenido.append({"mensaje_id": nodo_actual.mensaje_id, "valor": nodo_actual.valor})
            nodo_actual = nodo_actual.siguiente
        return contenido  # Devuelve la lista de mensajes

    def ver_ultimo(self):
        if self.ultimo:
            return {"mensaje_id": self.ultimo.mensaje_id, "valor": self.ultimo.valor}
        else:
            return None

    def ver_primero(self):
        if self.primero:
            return {"mensaje_id": self.primero.mensaje_id, "valor": self.primero.valor}
        else:
            return None

    def contar(self):
        count = 0
        nodo_actual = self.primero
        while nodo_actual:
            count += 1
            nodo_actual = nodo_actual.siguiente
        return count

    def eliminar_mensaje(self, mensaje_id: int):
        nodo_actual = self.primero
        nodo_anterior = None

        while nodo_actual and nodo_actual.mensaje_id != mensaje_id:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

        if nodo_actual:
            if nodo_anterior:
                nodo_anterior.siguiente = nodo_actual.siguiente
            else:
                self.primero = nodo_actual.siguiente

            if not nodo_actual.siguiente:
                self.ultimo = nodo_anterior

            return True

        return False
