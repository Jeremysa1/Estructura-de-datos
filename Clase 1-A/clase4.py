#funcion recursiva 

import random

def crear_lista(num_nodos):                                                            
    lista_generada = []                                                                 
    for _ in range(num_nodos):                                                          
        numero_aleatorio = random.randint(1, 100)                                       
        lista_generada.append(numero_aleatorio)                                         
    return lista_generada                                                               

num_nodos = int(input("Ingrese el número de nodos a crear: "))                          
lista_generada = crear_lista(num_nodos)                                                 
print("Lista generada:", lista_generada) 