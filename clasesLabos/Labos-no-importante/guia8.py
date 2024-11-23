from queue import LifoQueue as Pila, Queue as Cola

import random

# Ejercicio 1 

def generar_numeros_al_azar ( cantidad:int, desde:int, hasta:int) -> Pila[int]:
    respuesta: Pila[int] = Pila ()  
    while cantidad != 0:
        respuesta.put(random.randint(desde,hasta))
        cantidad -= 1
    return respuesta

pila_prueba: Pila[int] = generar_numeros_al_azar (5,0,3)
# print (pila_prueba) # No imprime ya que el print no está hecho para pilas o colas y no sabe qué quiero imprimir

# Hay que armarlo:

def mostrar_pila (pila:Pila[int]) -> None:    # lo que pasa es que pila de prueba va a terminar vacia 
    pila_aux: Pila[int] = Pila()
    while not pila.empty():
        elem: int = pila.get()
        print (elem)
        pila_aux.put (elem)
    while not pila_aux.empty():
        pila.put(pila_aux.get())
    print ("---")

'''
mostrar_pila (pila_prueba)
mostrar_pila (pila_prueba) 
'''

# Entonces hay que hacer un copy con una pila auxiliar para borrar esa y que la otra quede 
# PilaAuxiliar queda como pila pero exactamente dada vuelta entonces cuando metemos los elementos de nuevo en pila
# esta queda como estaba originalmente 

# Ejercicio 2
'''''
Ejercicio 2. Implementar una funci´on cantidad elementos(in p : Pila) → int que, dada una pila, cuente y devuelva la cantidad de elementos que contiene. 
No se puede utilizar la funci´on LifoQueue.qsize(). Si se usa get() para recorrer la pila, esto
modifica el par´ametro de entrada. Y como la especificaci´on dice que es de tipo in hay que restaurarla
'''
def cantidad_elementos (p: Pila[int]) -> int:
    res: int = 0
    pila_auxiliar : Pila [int] = Pila()
    while not p.empty():
        elemento: int = p.get()
        res += 1
        pila_auxiliar.put(elemento)
        mostrar_pila (p)
        print (res)
        mostrar_pila (pila_auxiliar)
        
    return res
    restaurar_pila(p,pila_auxiliar)
    mostrar_pila (p)
    mostrar_pila (pila_auxiliar)
    
    
def restaurar_pila (pila: Pila[int], auxiliar: Pila [int]) -> None:
    while not auxiliar.empty():
        
        elemento : int = auxiliar.get()
        pila.put(elemento)
        
        
pila_de_prueba : Pila [int] = generar_numeros_al_azar (10,0,3)
print(cantidad_elementos(pila_de_prueba))



# Ejercicio 3


def buscar_el_maximo (p:Pila[int]) -> int:
    pila_aux: Pila [int] = Pila()
    if p.empty():  # Si la pila esta vacia devuelvo 0
        return 0
    maximo:int = p.get() # Le asigno a maximo el primer elemento
    pila_aux.put(maximo) # como lo saqué ahora lo voy guardando
    while not p.empty(): 
        elementoActual: int = p.get() # Voy sacando de a 1 
        pila_aux.put(elementoActual) # Lo guardo
        if  maximo < elementoActual: # Comparo
            maximo = elementoActual
    while not pila_aux.empty(): # Armo mi pila original de nuevo
        p.put(pila_aux.get())
    return maximo

pila_prueba2: Pila [int] = generar_numeros_al_azar (5,0,3)

#print ("El maximo es " + str(buscar_el_maximo(pila_prueba2)))
#mostrar_pila (pila_prueba2)

# Ejercicio 13

def armar_secuencia_de_bingo () -> Cola[int]:
    mi_secuencia: Cola[int] = Cola ()
    mi_lista : list [int] = []
    for i in range (100):
        mi_lista.append(i)
    random.shuffle(mi_lista)
    for elem in mi_lista:
        mi_secuencia.put(elem)
    return mi_secuencia


'''''
mi_lista : list [int] = []
    for i in range (100):
        mi_lista.append(i)
Es lo mismo que
mi_lista : list [int] = range (100)
'''

# random.shuffle () es con listas 
# Para que no ocurra el error de que tenga numeros repetidos 

def mostrar_cola (cola:Cola[int]) -> None:
    cola_aux: Cola [int] = Cola ()
    while not cola.empty():
        elem: int = cola.get()
        print (elem)
        cola_aux.put(elem)
    while not cola_aux.empty():
        cola.put (cola_aux.get())
    print ("---")


#mostrar_cola(armar_secuencia_de_bingo())

# 2)
  
def jugar_carton_de_bingo (carton: list[int],bolillero: Cola[int]) -> int:
    cola_aux: Cola[int] = Cola()
    jugadas: int = 0
    coincidencias : int = 0
    while coincidencias < len(carton):
        elem: int = bolillero.get()
        cola_aux.put(elem)
        jugadas += 1
        if pertenece(elem,carton):
            coincidencias += 1
    while not bolillero.empty():
        cola_aux.put(bolillero.get())
    while not cola_aux.empty():
        bolillero.put(cola_aux.get())
    return jugadas 


# Ejercicio 17
'''''
def calcular_promedio_por_estudiante (notas: list[tuple[str,float]]) -> dict [str,float]:
    d : dict[str,float] =  {}
    for tupla in notas:
        if not tupla[0] in d:
            d [tupla[0]] = calcular_promedio(tupla[0]):
        return d
    
def calcular_promedio (alumno:str, notas: list [tuple[str,float]]) -> float:
        cant_notas: int = 0
        suma_notas: int = 0
        for nota in notas:
            if nota[0] == alumno:
                cant_notas += 1
                suma_notas += nota[1]
        return suma_notas/ cant_notas
    
    
 carton = armar_carton()
def armar_carton () -> list[int]:
    mi_lista : list [int] = []
    mi_carton: list [int] = []
    for i in range (100):
        mi_lista.append(i)
    random.shuffle(mi_lista)
    while len(mi_carton) != 4:
        for elem in mi_lista:
            mi_carton.append (elem)
    return mi_carton
    '''
