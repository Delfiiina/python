from queue import LifoQueue as Pila, Queue as Cola

import random


################################################


def mostrar_pila (pila:Pila[int]) -> None:     
    pila_aux: Pila[int] = Pila()
    while not pila.empty():
        elem: int = pila.get()
        print (elem)
        pila_aux.put (elem)
    while not pila_aux.empty():
        pila.put(pila_aux.get())
        
        
###############################################

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
        print ("la pila original:")
        mostrar_pila (p)
        elemento: int = p.get()
        res += 1
        pila_auxiliar.put(elemento)
        print ("La pila original queda:")
        mostrar_pila (p)
        print ("El contador por ahora va:")
        print (res)
        print ("La pila auxiliar se va llenando:")
        mostrar_pila (pila_auxiliar)
       
    restaurar_pila(p,pila_auxiliar)
    print ("mi pila original nuevamente como estaba:")
    mostrar_pila (p)
    print ("mi pila auxiliar que deberia estar vacía:")
    mostrar_pila (pila_auxiliar)
    
    print ("El largo de la pila es: " , res) 
    return res
  
######################################################################################
  
  
def restaurar_pila (pila: Pila[int], auxiliar: Pila [int]) -> None:
    while not auxiliar.empty():
        
        elemento : int = auxiliar.get()
        pila.put(elemento)
        

######################################################################################

pila_de_prueba : Pila [int] = Pila () 
for num in [3,2,1,0]:
    pila_de_prueba.put (num)
    
#print(cantidad_elementos(pila_de_prueba))


# Ejercicio 4

'''''
Dada una pila de tuplas de string x enteros, implementar una funci´on buscar nota maxima(in p : Pila[tuple[str, int]]) → 
que devuelva la tupla donde aparece la m´axima nota (segunda componente de la tupla). La pila no est´a vac´ıa, no hay valores en
las segundas posiciones repetidas en la pila.
'''

def buscar_nota_maxima (p:Pila[tuple[str,int]]) -> tuple[str,int]:
    
    tupla_max_actual : tuple[str,int] = p.get()
    print ("la tupla actual es ", tupla_max_actual)
        
    pila_auxiliar : Pila [tuple[str,int]] = Pila ()
    pila_auxiliar = pila_auxiliar.put(tupla_max_actual)
    print ("con la tupla que saque la pila auxiliar queda:")
    mostrar_pila (pila_auxiliar)
    while not p.empty():    
        actual : tuple[str,int] = p.get()
        pila_auxiliar.put(actual)
        print ("con la tupla que saque la pila auxiliar queda:")
        if actual[1] > tupla_max_actual [1]:
            tupla_max_actual = actual
            print ("ahora el maximo es ", tupla_max_actual)

    restaurar_pila (p,pila_auxiliar)
    print ("la nota máxima esta en la tupla: ", tupla_max_actual)
    return tupla_max_actual


pila_de_notas: Pila [tuple[str,int]] = Pila ()
for elem in [("a",7),("b",5),("c",9),("f",1)]:
    pila_de_notas.put(elem)
    
#print (buscar_nota_maxima(pila_de_notas))
        
   