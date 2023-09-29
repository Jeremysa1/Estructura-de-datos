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
        self.contador_id + = 1
    
    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.primero.valor
        mensaje_id = self.primero.mensaje_id 
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        return{"mensaje_id": mensaje_id, "valor": valor} #SE DEVUELVE EL MENSAJE DESENCOLADO

     def ver_listado(self):
        contenido[]
        actual = self.primero
        while contenido:
            contenido.append({"mensaje_id": actual.mensaje.id, "valor": self.primero.valor})
            actual = actual.siguiente 
            return contenido  #SE DEVUELVE LA LISTA DE MENSAJES 

     def ver ultimo(self):
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
        actual = self.primero
        while actual is not None:
            count += 1
            actual = actual.siguiente  
        return count  #.....
        

     def eliminar_mensaje(self, mensaje_id: int) -> bool:
        actual = self.primero
        anterior = None

        while actual and actual.mensaje_id != mensaje_id:
            anterior = actual
            actual = actual.siguiente

        if actual:
            if anterior:
             anterior.siguiente = actual.siguiente
            else:
                self.primero = actual.siguiente

            if not actual.siguiente:
                self.ultimo = anterior
            return True  # El mensaje se eliminó exitosamente

        return False  # El mensaje con el mensaje_id no se encontró en la cola
