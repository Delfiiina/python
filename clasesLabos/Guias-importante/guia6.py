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

def cantidad_de_pizzas (comensales: int, min_cant_de_porciones:int) -> int:
    pizza: int = comensales * min_cant_de_porciones
    if pizza % 8 == 0:
        res: int = pizza/8
    else:
        while pizza % 8 != 0:
            pizza += 1
        res: int = pizza/8
    return res

#print (cantidad_de_pizzas (9, 0))

# Ejercicio 3

# 1) 
def alguno_es_0 (numero1:int, numero2:int) -> bool:
    numeros : int = numero1 + numero2
    return numeros == numero1 or numeros == numero2
            
'''
print (alguno_es_0 (1,2)) # False
print (alguno_es_0 (0,1)) # True
print (alguno_es_0 (1,0)) # True
print (alguno_es_0 (0,0)) # True
'''
# 2)
def ambos_son_0 (numero1:int, numero2:int) -> bool:
    return (numero1 == 0 and numero2 == 0)
'''
print (ambos_son_0 (1,2)) #False 
print (ambos_son_0 (0,1)) #False
print (ambos_son_0 (1,0)) #False
print (ambos_son_0 (0,0)) #True
'''
# 4)
def es_bisiesto (ano:int) -> bool:
    return (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0))
'''
print (es_bisiesto (2024)) #True
print (es_bisiesto (2023)) #False
'''

# Ejercicio 4

def peso_pino (altura:float) -> float:
    if altura <= 3:
        res:float = (altura * 100)*3
    else:
        pino: float = altura - 3
        hola: float = pino * 100  * 2
        res: float = (3*300) + hola
    return res
'''
print (peso_pino (2.0))
print (peso_pino (3.0))
print (peso_pino (5.0))
print (peso_pino (0.0))
print (peso_pino (2.6))
'''
def es_peso_util (peso:float) -> bool:
    return (peso > 400 and peso < 1000)
'''
print (es_peso_util (0.0))
print (es_peso_util (400.0))
print (es_peso_util (400.1))
print (es_peso_util (999.9))
print (es_peso_util (1000.2))
'''
def sirve_pino (altura:float) -> bool:
    return (es_peso_util(peso_pino(altura)))

#print (sirve_pino (20.0))
#print (sirve_pino (47487584774857.0))
#print (sirve_pino (3.0))

# Ejercicio 5

def devolver_el_doble_si_es_par (numero:int) -> int:
    if numero % 2 == 0:
        return numero*2
    else:
        return numero

def devolver_valor_si_es_par_sino_el_que_sigue (numero:int) -> int:
    if numero % 2 == 0:
        return numero
    else:
        return numero + 1
    
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (numero:int) -> int:
    if numero % 3 == 0:
        return numero * 2
    elif numero % 9 == 0:
        return numero * 3
    else:
        return numero

def lindo_nombre (nombre: str):
    if len(nombre) >= 5:
        print ("tu nomrbrfayfr ")
    else:
        print ("menos de 5 dj") 

#lindo_nombre ("GGGGGG")
#lindo_nombre ("s")

def elRango (numero:int):
    if numero < 5 :
        print ("Menor a 5")
    elif numero > 10 and numero < 20:
        print ("jfjfhjfhjfhj")
    elif numero > 20:
        print ("jjhfttsf")
    
def argentina (sexo: str, edad:int):
    if edad < 18:
        print ("vaca")
    elif sexo == "M":
        if edad < 60:
            print ("pala")
        else:
            print ("vaca")
    else:
        if edad < 65:
            print ("pala")
        else:
            print ("vaca")

# Ejercicio 6
# 3)

def eco ():
    contador:int = 0
    while contador < 10:
        print ("eco")
        contador += 1

#eco ()

# 5)
def viajes_en_el_tiempo (partida:int, llegada:int):
    for i in range (partida,llegada-1,-1):
        print ("Viajo ncncnc estamos en el año: " + str(i))

# viajes_en_el_tiempo (20,10)

# 6)

def absoluto (numero:int) -> int:
    if numero < 0:
        return -numero
    else: return numero
    
def aristoteles (partida:int):
    par:int = partida
    while par > -384:
        print ("Viajo mucho " + str (par))
        par -= 20
    if (absoluto (par + 384)) < (absoluto ((par + 20) + 384)):
        print ("Viajo mucho " + str (par))
    else: 
        print ("Viajo mucho " + str (par + 20))

#aristoteles (10)


    
#print (absoluto (8))
#print (absoluto (0))
#print (absoluto (-7))
