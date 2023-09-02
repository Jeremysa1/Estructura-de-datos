#funcion recursiva 

import random
#importe la biblioteca random para generar números aleatorios y defini una clase llamada Nodoq ue representará un nodo en nuestra lista enlazada
class Nodo:
    def __init__(self, dato=None):   
        self.dato = dato
        self.siguiente = None

#La función crear_nodo_aleatorio se encarga de crear un nodo con un dato aleatorio generado por

def crear_nodo_aleatorio():
    numero = random.randint(0, 100)  # Genera un número entero aleatorio entre 0 y 100
    return Nodo(numero)

#La función crear_lista_nodos es una función recursiva que crea una lista enlazada de nodos. Le pasé el número deseado de nodos ( num_nodos) 

def crear_lista_nodos(num_nodos, cabeza=None):  #Cada vez que llamamos a esta función, crea un nuevo nodo aleatorio y lo enlaza al nodo anterior.
    if num_nodos == 0:
        return cabeza
    nuevo_nodo = crear_nodo_aleatorio()
    nuevo_nodo.siguiente = cabeza
    return crear_lista_nodos(num_nodos - 1, nuevo_nodo)

def obtener_datos_nodos(lista, datos=[]):  #La función obtener_datos_nodos es otra función recursiva que registra la lista enlazada y extrae los datos de cada nodo.
    if lista is None:
        return datos
    datos.append(lista.dato)
    return obtener_datos_nodos(lista.siguiente, datos)

# Uso de las funciones
num_nodos = 10  # Puedo cambiar este valor al número deseado de nodos que yo quiera
lista_cabeza = crear_lista_nodos(num_nodos)
datos_nodos = obtener_datos_nodos(lista_cabeza)
print(f"Nodos creados: {datos_nodos}")

