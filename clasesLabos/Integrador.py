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

print (generar_diccionario(palabras_separadas(r"C:\Delfina\python\apartePy\python\clasesLabos\conceptos1.txt",".")))

# 4) Implementar una función que, dados dos diccionarios como los del punto 3, devuelva una lista de dos listas de enteros, 
# donde cada una de las listas interiores corresponde a los índices correspondientes a los valores en común entre ambos. 
# Por ejemplo, si el diccionario A es {1:’silla’, 13: ‘canguro’} y B es {3:’canguro’, 9:’pera’}, la función devuelve [[13], [3]].

def indices_en_comun (diccionario1: dict[int,str], diccionario2: dict [int,str]) -> list[list[int]]:
    lista1 : list [int] = []
    lista2: list [int] = []
    res: list[list[int]] = []
    indice_actual: int = 0
    
    for par_clave_valor in diccionario1:
        indice_actual = par_clave_valor[0]
        if par_clave_valor[1] in diccionario2.values():
            lista1.append(par_clave_valor[0])
            lista2.append()
            
    