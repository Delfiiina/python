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

'''''
print (esta_bien_balanceada("(1+2)-2"))
print (esta_bien_balanceada("(1+2)-2)"))
print (esta_bien_balanceada("(1+2)-2*(5"))
print (esta_bien_balanceada("((1+2)-2)"))
'''

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
#print (evaluar_expresion("13 56 + 23 /"))
# Falta corregirlo 

# Ejercicio 7 

def intercalar (p1:Pila, p2:Pila) -> Pila:
    pila_res: Pila = Pila()
    pila_aux_1 : Pila = Pila () #Para restaurar al final
    pila_aux_2 : Pila = Pila () #Para restaurar al final
    pila_dadavuelta_1 : Pila = Pila ()
    pila_dadavuelta_2 : Pila = Pila ()

    while not p1.empty():  # Tendría que quedar la pila dada vuelta (lo que me sirve)
        elem : int = p1.get()
        pila_aux_1.put(elem)
        pila_dadavuelta_1.put(elem)
        
    while not p2.empty():  # Tendría que quedar la pila dada vuelta (lo que me sirve)
        elem : int = p2.get()
        pila_aux_2.put(elem)
        pila_dadavuelta_2.put(elem)
        
    while (not pila_dadavuelta_1.empty()) and (not pila_dadavuelta_2.empty()):
        elemto_a_meter: int = pila_dadavuelta_1.get()
        pila_res.put(elemto_a_meter)
        elemto_a_meter = pila_dadavuelta_2.get()
        pila_res.put(elemto_a_meter)
        
    restaurar_pila (p1,pila_aux_1)
    restaurar_pila (p2, pila_aux_2)
    
    return pila_res    
''''      
pilita1 = Pila ()
pilita1.put(1)
pilita1.put(2)
pilita1.put(3)
pilita1.put(4)

pilita2 = Pila ()
pilita2.put(5)
pilita2.put(6)
pilita2.put(7)
pilita2.put(8)

print ("mi pila1 original: ")
print (pilita1.queue)
print ("mi pila 2 original: ")
print (pilita2.queue)

print ("Ahora la función: ")
print (intercalar(pilita1,pilita2).queue)
print ("mi pila1 que debería estar igual:")
print (pilita1.queue)
print ("mi pila2 que debería estar igual:")
print (pilita2.queue)
'''''

# Ejercicios de colas-

#######################################################


def restaurar_cola (cola:Cola, auxiliar:Cola) -> Cola:
    #la cola va a estar vacía y auxiliar va a tener todos los elementos ordenados.
    
    while not auxiliar.empty():
        elemento = auxiliar.get()
        cola.put(elemento)
        
    return cola


########################################################    

# Ejercicio 8

def generar_nros_al_azar (cantidad: int, desde: int, hasta:int) -> Cola:
    res: Cola = Cola()
    cantidadd : int = cantidad # los int los pasa por copia, entonces no modifiqué a cantidad (que era in)
    
    while cantidadd > 0:
        res.put(random.randint(desde,hasta))
        cantidadd -= 1
    
    return res

#print (generar_nros_al_azar(15,1,9).queue)

# Ejercicios 9

def cantidad_elementos (c:Cola) -> int:
    lista : list[int] = []
    cola_auxiliar : Cola = Cola()
    
    while not c.empty():
        elemento : int = c.get()
        cola_auxiliar.put(elemento)
        lista.append(elemento)
        
    return len(lista)


colaw = Cola()
colaw.put(1)
colaw.put(2)
colaw.put(1)
colaw.put(4)
colaw.put(9)
#print (cantidad_elementos(colaw))
        
# Ejercicio 10

def buscar_el_maximo (c:Cola[int]) -> int:
    cola_auxiliar : Cola[int] = Cola()
    
    maximo : int = c.get()
    cola_auxiliar.put(maximo)
    
    while not c.empty():
        elemento : int = c.get()
        cola_auxiliar.put(elemento)
        if maximo < elemento:
            maximo = elemento
            
    respuesta : int = maximo
    restaurar_cola(c,cola_auxiliar)    
    return respuesta

#print (buscar_el_maximo(colaw))

# Ejercicio 11

def buscar_nota_minima (c: Cola[str,int]) -> tuple[str,int]:
    cola_auxiliar: Cola[str,int] = Cola()
    
    nota_minima : tuple[str,int] = c.get()
    cola_auxiliar.put(nota_minima)
    
    while not c.empty():
        elemento : tuple[str,int] = c.get()
        cola_auxiliar.put(elemento)
        if nota_minima[1] > elemento[1]:
            nota_minima = elemento
        
    restaurar_cola(c, cola_auxiliar)
    return nota_minima

cola_de_notas = Cola()
cola_de_notas.put(("a",7))
cola_de_notas.put(("b",4))
cola_de_notas.put(("c",8))
cola_de_notas.put(("d",10))
cola_de_notas.put(("e",9))

#print (buscar_nota_minima(cola_de_notas))

# Ejercicio 12

def intercalar_c (c1:Cola[int], c2:Cola[int]) -> Cola[int]:
    # la diferencia con el ej de pilas es que como son colas no tengo que darla vuelta
    cola1_aux : Cola[int] = Cola ()
    cola2_aux : Cola[int] = Cola ()
    respuesta : Cola[int] = Cola ()
    
    while not c2.empty():
        elemento1 : int = c1.get()
        cola1_aux.put(elemento1)
        respuesta.put(elemento1)
        elemento2: int = c2.get()
        cola2_aux.put(elemento2)
        respuesta.put(elemento2)
    
    restaurar_cola(c1,cola1_aux)
    restaurar_cola(c2,cola2_aux)
    
    return respuesta

cola11 = Cola()
cola11.put(1)
cola11.put(1)

cola22 = Cola()
cola22.put(2)
cola22.put(2)

#print (intercalar_c(cola11,cola22).queue)

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

#print (existe_palabra("hola", "hola.txt"))


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