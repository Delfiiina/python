import math

# Ejercicio 1
# 1)

def imprimir_hola_mundo ():
    print ("hola mundo")

# 2)

def imprimir_un_verso ():
    print ("hola\nchau")

# 3)

def raiz_de_2 () -> float:
    return (round (math.sqrt (2)) ,4)

# 4)

def factorial_de_2 () -> int: # lo voy a poner con 4 pq con 2 es igual a 2 y es como no hacer nada 
    return math.factorial (4)


def factorial_de_numero (numero:int) -> int:
        return math.factorial (numero)

# 5)

def perimetro () -> float:
    return (2*(math.pi))

def perimetro2 () -> float:
    res: float = 2 * math.pi
    return res

respuesta : float = perimetro ()
# la guarde globalmente 
# res es una variable local

# Ejercicio 2
# 1)
def imprimir_saludo (nombre:str):
    print ("Hooooola " + nombre)

# 2)

def raiz_cuadrada_de (numero: int):
    return math.sqrt (numero)

# 3)

def fahrenheit_a_celsius (f:int):
    return ((f-32)*5)/9

# 4)

def imprimir_dos_veces (estribillo: str):
    print (estribillo * 2)

def imprimir_dos_veces_v2 (estribillo: str):
    print (estribillo + estribillo)

# 5)

def es_multiplo_de (n: int, m:int) -> bool :
    if m % n == 0 : 
        return True
    else:
        return False
    
def es_multiplo_de_v2 (n:int, m:int) -> bool :
    return (m % n == 0)

def es_multiplo_de_v3 (n:int, m:int) -> bool:
    if m%n == 0:
        res : bool = True
    else :
        res : bool = False
    return res

def es_multiplo_de_v4 (n:int, m:int) -> bool:
    res: bool = True
    if m%n != 0 :
        res = False
    return res  

# 6)

def es_par (numero:int) -> bool:
    return es_multiplo_de (2,numero)

# 7)

def cantidad_de_pizzas (comensales:int, min_cant_porciones:int) -> int:
    cantidad_de_pizza :int = comensales * min_cant_porciones / 8
    if cantidad_de_pizza % 8 == 0:
        return (cantidad_de_pizza)
    else:
        return (cantidad_de_pizza) 


def es_nombre_largo (nombre: str) -> bool:
    return  len (nombre) >= 3 and len (nombre) <= 8

def devolver_el_doble_si_es_par (numero: int) -> int:
    if numero % 2 == 0:
        res: int = numero * 2
    else:
        res: int = numero
    return res 

# Ejercicio 6

def numeros_pares_10_40 ():
    x: int = 10
    while x <= 40:
        if x % 2 == 0:
            print (x)
        x += 1

def cuenta_regresiva (numero:int):
    while numero != 0:
        print (numero)
        numero -= 1
    print ("fduhfi")

def numeros_pares_10_40_v2 ():
    for x in range (10,41,2):
        print (x)

def cuenta_regresiva_v2 (numero:int):
    for n in range (numero,0,-1):
        print (n)
    print ("dgj")

# print (cuenta_regresiva(8))
