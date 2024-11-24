from queue import LifoQueue as Pila, Queue as Cola
from typing import List, TextIO
import random
import math
"""
1) Juego del gallina (3 puntos)
El juego del gallina es una competición en la que dos participantes conducen un vehículo en dirección al del contrario;
si alguno se desvía de la trayectoria de choque pierde y es humillado por comportarse como un "gallina". 
Se hizo un torneo para ver quién es el menos gallina. Juegan todos contra todos una vez y van sumando puntos, o restando. 
Si dos jugadores juegan y se chocan entre sí, entonces pierde cada uno 5 puntos por haberse dañado. 
Si ambos jugadores se desvían, pierde cada uno 10 puntos por gallinas. 
Si uno no se desvía y el otro sí, el gallina pierde 15 puntos por ser humillado y el ganador suma 10 puntos! 
En este torneo, cada persona que participa tiene una estrategia predefinida para competir: o siempre se devía, o nunca lo hace.
Se debe programar la función 'torneo_de_gallinas' que recibe un diccionario 
(donde las claves representan los nombres de los participantes que se anotaron en el torneo, y los valores sus respectivas estrategias) 
y devuelve un diccionario con los puntajes obtendidos por cada jugador.

problema torneo_de_gallinas (in estrategias: dict⟨String,String⟩) : dict⟨String,Z⟩ {
  requiere: {estrategias tiene por lo menos 2 elementos (jugadores)}
  requiere: {Las claves de estrategias tienen longitud mayor a 0}
  requiere: {Los valores de estrategias sólo pueden ser los strings "me desvio siempre" ó "me la banco y no me desvio"}
  asegura: {Las claves de res y las claves de estrategias son iguales}
  asegura: {para cada jugador p perteneciente a claves(estrategias), res[p] es igual a la cantidad de puntos que obtuvo al finalizar el torneo, dado que jugó una vez contra cada otro jugador}
}

2) Cola en el Banco (1 puntos)
En el banco ExactaBank los clientes hacen cola para ser atendidos por un representante. Los clientes son representados por las tuplas (nombre, tipo afiliado) donde la primera componente es el nombre y el tipo afiliado puede ser "comun" o "vip".
Se nos pide implementar una función en python que dada una cola de clientes del banco, devuelva una nueva cola con los mismos clientes pero en donde los clientes vip estan primero que los clientes comunes manteniendo el orden original de los clientes vips y los comunes entre sí.


problema reordenar_cola_priorizando_vips (in filaClientes: Cola⟨String x String⟩) : Cola⟨String⟩ {
  requiere: {La longitud de los valores de la primera componente de las tuplas de la cola filaClientes es mayor a 0}
  requiere: {Los valores de la segunda componente de las tuplas de la cola filaClientes son "comun" o "vip" }
  requiere: {No hay dos tuplas en filaClientes que tengan la primera componente iguales entre sí }
  asegura: {todo valor de res aparece como primera componente de alguna tupla de filaClientes}
  asegura: {|res| = |filaCliente|}
  asegura: {res no tiene elementos repetidos}
  asegura: {No hay ningun cliente "comun" antes que un "vip" en res}
  asegura: {Para todo cliente c1 y cliente c2 de tipo "comun" pertenecientes a filaClientes si c1 aparece antes que c2 en filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res}
  asegura: {Para todo cliente c1 y cliente c2 de tipo "vip" pertenecientes a filaClientes si c1 aparece antes que c2 en filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res}
}

Nota: un sufijo es una subsecuencia de texto que va desde una posición cualquiera hasta el al final de la palabra. Ej: "Diego", el conjunto de sufijos es: "Diego", "iego","ego","go", "o". Para este ejercicio no consideraremos a "" como sufijo de ningun texto.
4) Ta-Te-Ti-Facilito (2 puntos)
Ana y Beto juegan al Ta-Te-Ti-Facilito. El juego es en un tablero cuadrado de lado entre 5 y 10. Cada jugador va poniendo su ficha en cada turno. Juegan intercaladamente y comienza Ana. Ana pone siempre una 'X' en su turno y Beto pone una 'O' en el suyo. Gana la persona que logra poner 3 fichas suyas consecutivas en forma vertical. Si el tablero está completo y no ganó nadie, entonces se declara un empate. El tablero comienza vacío, representado por ' ' en cada posición.
Notar que dado que juegan por turnos y comienza Ana poniendo una 'X' se cumple que la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' son uno más que la cantidad de 'O'.
Se nos pide implementar una función en python 'problema quien_gano_el_tateti_facilito' que determine si ganó alguno, o si Beto hizo trampa (puso una 'O' cuando Ana ya había ganado).

problema quien_gano_el_tateti_facilito(in tablero:seq⟨seq⟨Char⟩) : Z {
  requiere: {tablero es una matriz cuadrada}
  requiere: {5<=|tablero[0]|<= 10}
  requiere: {tablero sólo tiene 'X', 'O' y ' ' (espacio vacío) como elementos}
  requiere: {En tablero la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' es uno más que la cantidad de 'O'}
  asegura: {res = 1 <==> hay tres 'X' consecutivas en forma vertical(misma columna) y no hay tres 'O' consecutivas en forma vertical(misma columna) }
  asegura: {res = 2 <==> hay tres 'O' consecutivas en forma vertical (misma columna) y no hay tres 'X' consecutivas en forma vertical(misma columna) }
  asegura: {res = 0 <==> no hay tres 'O' ni hay tres 'X' consecutivas en forma vertical}
  asegura: {res = 3 <==> hay tres 'X' y hay tres 'O' consecutivas en forma vertical (evidenciando que beto hizo trampa)}
}
"""
# Ejercicio 1

def cuanto_saco (persona_estrategia : tuple[str,str], estrategias: list[tuple[str,str]]) -> int:
    puntos : int = 0
    
    for tupla in estrategias:
        if tupla != persona_estrategia:
            if persona_estrategia[1] == tupla [1]:
                if persona_estrategia[1] == "me desvio siempre":
                    puntos -= 10
                else:
                    puntos -= 5
            else:
                if persona_estrategia[1] == "me desvio siempre":
                    puntos -= 15
                else:
                    puntos +=10
    return puntos 
    
    
def torneo_de_gallinas (estrategias: dict[str,str]) -> dict[str,int]:
    diccionario : dict [str,int] = {}
    
    for persona in estrategias.keys():
        diccionario[persona] = 0
        
    for tupla in estrategias.items():
        diccionario[tupla[0]] = cuanto_saco(tupla,estrategias.items())
    
    return diccionario

##################################################################
"""
diccionario = { "Juan" : "me desvio siempre",
               "Martin" : "me la banco y no me desvio",
               "Lucio" : "me la banco y no me desvio",
               "Fran" : "me desvio siempre",
               "T" : "me la banco y no me desvio"
               }
print (torneo_de_gallinas(diccionario))
"""
#####################################################################

# Ejercicio 2

def reordenar_cola_priorizando_vips (filaClientes: Cola[tuple[str,str]]) -> Cola[str]:
    res : Cola [str] = Cola ()
    filaClientes_aux : Cola [tuple[str,str]] = Cola()
    clientesVIP : Cola [str] = Cola()
    clientesComunes : Cola [str] = Cola()
     
    while not filaClientes.empty():
        elemento : tuple[str,str] = filaClientes.get()
        filaClientes_aux.put(elemento)
        if elemento[1] == "vip":
            clientesVIP.put(elemento[0])
        else:
            clientesComunes.put(elemento[0])
            
    while not filaClientes_aux.empty():
        sacar : tuple[str,str] = filaClientes_aux.get()
        filaClientes.put(sacar)
    
    while not clientesVIP.empty():
        elem : str = clientesVIP.get()
        res.put(elem)
        
    while not clientesComunes.empty():
        elem : str = clientesComunes.get()
        res.put(elem)
    
    return res
          
######################################################################################
'''  
filaClientes = Cola()
filaClientes.put (("Juan","vip"))
filaClientes.put (("Martin","vip"))
filaClientes.put (("Lucio","comun"))
filaClientes.put (("Martina","comun"))
filaClientes.put (("Julieta","vip"))
filaClientes.put (("Malena","comun"))
filaClientes.put (("Sofia","vip"))
filaClientes.put (("Euge","vip"))
print (reordenar_cola_priorizando_vips(filaClientes).queue)
'''
#####################################################################################

# Ejercicio 3

def es_palindromo (t:list[str]) -> bool:
    pila : Pila[str] = Pila()
    palabra_dada_vuelta : list[str] = []
    
    for caracter in t:
        pila.put(caracter)
    
    while not pila.empty():
        elem : str = pila.get()
        palabra_dada_vuelta.append(elem)
    
    if t == palabra_dada_vuelta:
        return True
    
    return False

def cuantos_sufijos_son_palindromos (texto:str) -> int: 
    contador : int = 0
    palabra_lista : list[str] = []
    
    for caracter in texto:
        palabra_lista.append(caracter)
    
    while palabra_lista != []:
        if es_palindromo(palabra_lista):
            contador += 1
        palabra_lista.pop()
    
    return contador

#####################################################
"""
palabra = "hola" #1
palabra2= "babab" #3
print (cuantos_sufijos_son_palindromos(palabra2))
"""
#####################################################

# Ejercicio 4
"""
problema quien_gano_el_tateti_facilito(in tablero:seq⟨seq⟨Char⟩) : Z {
  requiere: {tablero es una matriz cuadrada}
  requiere: {5<=|tablero[0]|<= 10}
  requiere: {tablero sólo tiene 'X', 'O' y ' ' (espacio vacío) como elementos}
  requiere: {En tablero la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' es uno más que la cantidad de 'O'}
  asegura: {res = 1 <==> hay tres 'X' consecutivas en forma vertical(misma columna) y no hay tres 'O' consecutivas en forma vertical(misma columna) }
  asegura: {res = 2 <==> hay tres 'O' consecutivas en forma vertical (misma columna) y no hay tres 'X' consecutivas en forma vertical(misma columna) }
  asegura: {res = 0 <==> no hay tres 'O' ni hay tres 'X' consecutivas en forma vertical}
  asegura: {res = 3 <==> hay tres 'X' y hay tres 'O' consecutivas en forma vertical (evidenciando que beto hizo trampa)}
"""

def transponer (tablero:list[list[str]]) -> list[list[str]]:
    res : list[list[str]] = []
    listita :list[str] = []
    for i in range (len(tablero)):
        for lista in tablero:
            listita.append(lista[i])
        res.append(listita)
        listita = []
    return res

tablero = [[" "," "," "," "," "],["X","O"," "," "," "],["X"," ","O"," "," "],["X"," "," "," "," "],[" "," "," "," "," "]]
#print (transponer(tablero))
tablero_transpuesto = [[' ', 'X', 'X', 'X', ' '], [' ', 'O', ' ', ' ', ' '], [' ', ' ', 'O', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]

def gano_alguien (letra: str, tablero_transpuesto : list[list[str]]) -> bool:
    
    for columna in tablero_transpuesto:
        for i in range (len(columna)-2):
            if columna[i] == letra and columna[i] == columna[i+1] and columna[i] == columna[i+2]:
                return True
    return False

#print (gano_alguien("X",tablero_transpuesto))


def quien_gano_el_tateti_facilito (tablero:list[list[str]]) -> int:
    transpuesta : list[list[str]] = transponer(tablero)
    
    if gano_alguien("X",transpuesta) == True and gano_alguien("O",transpuesta) == True:
        return 3
    elif gano_alguien ("X", transpuesta) == True and gano_alguien("O",transpuesta) == False:
        return 1
    elif gano_alguien ("X", transpuesta) == False and gano_alguien("O",transpuesta) == True:
        return 2
    else:
        return 0
    
############ De los profes
def palindromo(texto:str)->bool:
    for i in range(len(texto)//2):
        if (texto[i]!=texto[len(texto)-i-1]):
            return False
    return True
        