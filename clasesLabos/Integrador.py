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
    
    for caracter in datos: #Por cada caracter que hay en mi str
        if caracter == "." or caracter == ";":
            respuesta.append(palabra_actual) # Por cada punto (cada palabra) meto a la lista la palabra que ya fui guardando y también el caracter 
            respuesta.append (caracter) # No sé si puedo ponerlo todo junto o tengo que hacer 2 append's
            palabra_actual = "" # borro palabra 
        else:
            palabra_actual += caracter # Voy guardando cada palabra
    respuesta.append(palabra_actual)
    archivo.close() # Cierro el archivo
    return respuesta
    
print (palabras_separadas("integradorEjs.txt","m"))

# Si entendí bien el ejercicio tendría que funcionar(??) Pero no puedo probarlo.
# ["banana","m","manzana","m","jugo","m","pera","m","uva"]

# Utilizar la función anterior para los dos archivos provistos y generar una lista de strings para cada uno
    
# Sin separar por nada(?)
  