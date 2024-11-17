from queue import LifoQueue as Pila, Queue as Cola
from typing import List, TextIO
import random


# 1) Implementar una función que tome como entrada un archivo txt y un carácter y devuelva una lista de las palabras que se encuentran en el archivo,
# separadas por el carácter de entrada.

# En conceptos1 cada palabra está separada por un punto y en conceptos2, por un punto y coma
# Todas las palabras están en la misma línea


def palabras_separadas (nombre_archivo: str, caracter: str ) -> list [str]:
    archivo : TextIO = open (nombre_archivo, "r") # Abro el archivo de texto
    datos: str = archivo.readline() # Leo toda la linea. Es un string
    respuesta: list[str] = []
    palabra_actual: str = ""
    
    for letra in datos: #Por cada caracter que hay en mi str
        if letra == caracter:
            respuesta.append(palabra_actual) # Por cada palabra, la meto a la lista ya que la fui guardando 
            palabra_actual = "" # borro palabra 
        else:
            palabra_actual += letra # Voy guardando cada palabra
    respuesta.append(palabra_actual)
    archivo.close() # Cierro el archivo
    return respuesta

#prueba = palabras_separadas ("conceptos1.txt",".")
#print (prueba)


# 2) Utilizar la función anterior para los dos archivos provistos y generar una lista de strings para cada uno

#print (palabras_separadas(r"C:\Delfina\python\apartePy\python\clasesLabos\conceptos1.txt","."))
#print (palabras_separadas(r"C:\Delfina\python\apartePy\python\clasesLabos\conceptos2.txt",";"))

# 3) Generar dos diccionarios, uno para cada lista del punto 2, donde la clave sea el índice de la palabra en la lista y el valor sea la palabra.

def generar_diccionario (lista_de_palabras : list[str]) -> dict[int,str]:
    indice: int = 0 # el índice tiene que empezar en 0
    diccionario : dict [int,str] = {}  
    
    
    for palabra in lista_de_palabras:
        diccionario [indice] = palabra # como el índice no se va a repetir, no hace falta chequear si ya está la clave 
        indice += 1
    
    return diccionario

#print (generar_diccionario(palabras_separadas(r"C:\Delfina\python\apartePy\python\clasesLabos\conceptos1.txt",".")))


# Ejercicio 4    
# Implementar una función que, dados dos diccionarios como los del punto 3, 
# devuelva una lista de dos listas de enteros, donde cada una de las listas interiores 
# corresponde a los índices correspondientes a los valores en común entre ambos.
#  Por ejemplo, si el diccionario A es {1:’silla’, 13: ‘canguro’, 18: 'a'} y B es {3:’canguro’, 9:’pera’, 10: 'a'},
#  la función devuelve [[13,18], [3,10]].

def lista_de_repetidos (a: dict[int,str], b: dict[int,str]) -> list[list[int]]:
    res : list[list[int]] = []
    repetidos_a : list [int] = []
    repetidos_b : list [int] = []

    for tupla in a.items():
        clave_guardada : int = tupla[0]
        for tupla_dict2 in b.items():
            clave_del_dict2 :int = tupla_dict2[0]
            if tupla_dict2[1] == tupla[1]:
                repetidos_a.append (clave_guardada)
                repetidos_b.append (clave_del_dict2)
    
    res.append(repetidos_a)
    res.append(repetidos_b)

    return res 

diccionario_a = {
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d"
}

diccionario_b = {
    0 : "d",
    1 : "l",
    2 : "e",
    3 : "f"
}

#print (lista_de_repetidos(diccionario_a, diccionario_b))

# Ejercicio 5
# Generar una lista con todos los elementos presentes en los dos archivos txt,
# sin repeticiones (es decir, todos los que aparecen, una vez cada uno).
# Para esto, se pueden usar las listas o diccionarios de los puntos anteriores.

def todos_elementos_sinrepes (a: str, b: str) -> list[str]:
    res : list [str] = []

    for palabra in palabras_separadas(a,"."):
        res.append (palabra)
    
    for palabra_b in palabras_separadas(b,";"):
        if palabra_b not in res:
            res.append(palabra_b)

    return res

# Armar un pertenece
#print (todos_elementos_sinrepes("conceptos.txt","conceptos2.txt"))


# Ejercicio 6
# Implementar una función que tome dos listas de enteros (A y B) y
# una lista de listas de enteros (la del punto 4, llamada REP) y 
# devuelva una lista de listas de enteros, donde cada una es la lista original 
# sin la mitad de sus repetidos, alternando cuál se quita para cada lista. 
# Ejemplo: si REP es [[0,1,3,12],[0,14,19,22]] una solución posible es dejar [0,3] 
# en A y [14,22] en B junto al resto de los índices de elementos únicos de cada una de las listas.
            
    
def sacar_mitad_repetidos (a:list[int], b:list[int], rEP: list[list[int]]) -> list[list[int]]:
    res : list[list[int]] = []
    
    