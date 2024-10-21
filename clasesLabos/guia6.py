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

print (sirve_pino (20.0))
print (sirve_pino (47487584774857.0))
print (sirve_pino (3.0))

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

lindo_nombre ("GGGGGG")
lindo_nombre ("s")

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
def aristoteles (partida:int):
    par:int = partida
    while par > -384:
        print ("Viajo mucho" + str (par))
        par -= 20
    # if par 

aristoteles (10)