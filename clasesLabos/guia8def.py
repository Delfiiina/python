from queue import LifoQueue as Pila, Queue as Cola
from typing import List, TextIO
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

# Ejercicio 1

def generar_numeros_al_azar ( cantidad:int, desde:int, hasta:int) -> Pila[int]:
    respuesta: Pila[int] = Pila ()  
    while cantidad != 0:
        respuesta.put(random.randint(desde,hasta))
        cantidad -= 1
    return respuesta

pila_prueba: Pila[int] = generar_numeros_al_azar (5,0,3)
# print (pila_prueba) # No imprime ya que el print no está hecho para pilas o colas y no sabe qué quiero imprimir

'''
mostrar_pila (pila_prueba)
mostrar_pila (pila_prueba) 
'''


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

# Ejercicio 5

def esta_bien_balanceada (s:str) -> bool:
    pila: Pila = Pila()
    
    for caracter in s:
        if caracter == "(":
            pila.put(caracter)
        elif caracter == ")":
            if not pila.empty():
                pila.get()
            else:
                return False
                break
    return (pila.empty())

print (esta_bien_balanceada("(1+2)-2"))
print (esta_bien_balanceada("(1+2)-2)"))
print (esta_bien_balanceada("(1+2)-2*(5"))
print (esta_bien_balanceada("((1+2)-2)"))

# Ejercicio 6


def hacer_cuenta (s: str, m:str, a: str) -> float:
    elemento1 : float = float(s)
    elemento2 : float = float(m)
    res : float = 0

    if a == "+":
        res = elemento1 + elemento2
    elif a == "-":
        res = elemento2 - elemento1
    elif a == "*":
        res = elemento1 * elemento2
    else:        
        res = elemento2 / elemento1
    
    return res 


def evaluar_expresion (s: str) -> float:
    operandos : Pila = Pila()
    operadores : Pila = Pila ()
    contador_operadores : int = 0
    vacio : str = ""

    for caracter in s:
        if caracter not in ["+","-","*","/"]:
            vacio += caracter
        elif caracter in ["+","-","*","/"]:
          operadores.put(caracter)   
          contador_operadores += 1
          if contador_operadores == 1:
            elemento1 : str = operandos.get()
            elemento2 : str = operandos.get()
            operador1 : str = operadores.get()
            calculo: float = hacer_cuenta(elemento1,elemento2,operador1)
            operandos.put(calculo)
            operadores = Pila ()
            contador_operadores = 0       
        elif caracter == " ":
            operandos.put(vacio)
            vacio = ""
    
    return operandos.get()


#print (evaluar_expresion("1 1 + 5 * 3 + 7 /"))
#print (evaluar_expresion("1 6 + 8 * 2 /"))
print (evaluar_expresion("13 56 + 23 /"))
# Falta corregirlo 

# Ejercicio 7 FALTA
# Ejercicios de colas-
# Ejercicio 8
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