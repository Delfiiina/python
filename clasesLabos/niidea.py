from typing import List, TextIO


def contar_lineas (nombre_archivo: str) -> int:
    archivo : TextIO = open (nombre_archivo,"r", encoding= "utf-8")
    contador : int = 0
    
    for linea in archivo:   
        contador += 1
    
    archivo.close() 
    return contador

#print (contar_lineas ("hola.txt"))

def contar_lineas_v2 (nombre_archivo: str) -> int:
    archivo : TextIO = open (nombre_archivo,"r", encoding= "utf-8")
    lineas: int = len(archivo.readlines())
    archivo.close() 
    return lineas

#print (contar_lineas_v2 ("hola.txt"))



def imprimir_lineas (archivo: str):
    archivo: TextIO = open ("hola.txt","r", encoding = "utf-8")
    lineas : str = archivo.readlines()
    
    for linea in lineas:
        print (linea)

#imprimir_lineas("hola.txt")


# Ejercicio 2


def existe_palabra (palabra: str, nombre_archivo:str) -> bool:
    archivo : TextIO = open (nombre_archivo,"r", encoding = "utf-8")
    lineas : list[str] = archivo.readlines()
    listas : list[str] = []
    palabra : str = ""
    
    for linea in lineas:
        for letra in linea:
            if letra == " " or letra == "\n":
                listas.append(palabra) 
                palabra = ""
            else:
                palabra += letra
    
    print (listas)
    archivo.close()
    return palabra in listas    

print (existe_palabra("hola", "hola.txt"))


# Ejercicio 16 

def agrupar_por_longitud (nombre_archivo: str) -> dict:
    archivo : TextIO = open (nombre_archivo, "r")
    lineas : list[str] = archivo.readlines()
    diccionario : dict[int,int] = {}
    palabra : str = ""
    todas_las_palabras : list[str] = []
    
    for linea in lineas:
        for letra in linea:
            if letra == " " or letra == "\n":
                todas_las_palabras.append(palabra)
                palabra = ""
            else:
                palabra += letra
        print(todas_las_palabras)
    todas_las_palabras.append(palabra)


    for cada_palabra in todas_las_palabras:
        largo: int = len (cada_palabra)
        if largo not in diccionario.keys():
            diccionario[largo] = 1
        else:
            diccionario[largo] += 1
            
    return diccionario

#print (agrupar_por_longitud("hola.txt"))
            