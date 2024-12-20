from queue import LifoQueue as Pila, Queue as Cola
from typing import List, TextIO
import random
import math

''' Ejercicio 1

  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
    requiere: {e pertenece a s }
    asegura: {res es la posición de la última aparición de e en s}
  }

 Por ejemplo, dados
   s = [-1,4,0,4,100,0,100,0,-1,-1]
   e = 0
 se debería devolver res=7

 Ejercicio 2

  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
    requiere: -
    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
    asegura: {res no tiene elementos repetidos }
  }

 Por ejemplo, dados
   s = [-1,4,0,4,3,0,100,0,-1,-1]
   t = [0,100,5,0,100,-1,5]
 se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
 ó res = [5,3,4] ó res = [5,4,3]

 Ejercicio 3

 Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
 en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
 en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
 palabras que tienen la misma traducción en inglés y en alemán.

  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
    requiere: -
    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
  }

  Por ejemplo, dados los diccionarios
    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
  se debería devolver res=2

 Ejercicio 4

 Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
 y sus valores la cantidad de veces que cada uno de esos números aparece en s

  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
    requiere: -
    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
  }

  Por ejemplo, dada la lista
  lista = [-1,0,4,100,100,-1,-1]
  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
  
 RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO
'''

# Ejercicio 1

def  ultima_aparicion (s:list[int], e:int) -> int:
    pila : Pila[int] = Pila()
    
    for i in range (0,len(s),1):
        if e == s[i]:
            pila.put(i)
    
    return pila.get()
    
#s = [-1,4,0,4,100,0,100,0,-1,-1]
#e = 0
#print (ultima_aparicion(s,e))

# Ejercicio 2

def pertenece (numero: int, lista: list[int]) -> bool:
    for num in lista:
        if num == numero:
            return True
    return False

def elementos_exclusivos (s: list[int], t: list[int]) -> list[int]:
    
    res : list[int] = []
    
    for numero in s:
        if not pertenece (numero, res):
            if not pertenece (numero,t):
                res.append(numero)
    
    for numero in t:
        if not pertenece (numero, res):
            if not pertenece (numero,s):
                res.append(numero)
    
    return res

#s = [-1,4,0,4,3,0,100,0,-1,-1]
#t = [0,100,5,0,100,-1,5]
#print (elementos_exclusivos(s,t)) 

# Ejercicio 3

def contar_traducciones_iguales (ing: dict[str,str], ale: dict[str,str]) -> int:
    contador : int = 0
    
    for word in ing.keys():
        if pertenece (word,ale.keys()):
            if ing[word] == ale[word]:
                contador += 1
    return contador


#aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#print (contar_traducciones_iguales(inglés,aleman))            
    
# Ejercicio 4

def cantidad_apariciones (numero: int, lista: list[int]) -> int:
    contador : int = 0
    
    for num in lista:
        if num == numero:
            contador += 1
    return contador

def convertir_a_diccionario (lista:list[int]) -> dict[int,int]:
    diccionario : dict[int,int] = {}
    
    for numero in lista:
        if not pertenece (numero,diccionario.keys()):
            diccionario[numero] = cantidad_apariciones(numero,lista)
    
    return diccionario

lista = [-1,0,4,100,100,-1,-1]
print (convertir_a_diccionario(lista))
# debería devolver res={-1:3, 0:1, 4:1, 100:2}