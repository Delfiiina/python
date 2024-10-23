from typing import List, Dict, Tuple

# Ejercicio 1
# 1)

def pertenece (numero:int, lista:List[int]) -> bool:
    i: int = 0
    mi_numero : int = numero
    mi_lista : List = lista
    if mi_numero == mi_lista [i] : 
        return True 
        i += 1
    else :
        return False

#print (pertenece (5, [1,2,3]))

def pertenece2 (e:int, s:List [int]) -> bool:
    mi_numero : int = e
    mi_lista : List = s
    for i in range (0,len(mi_lista),1):
        if mi_lista[i] == mi_numero:
            return True 
    return False
        
#print (pertenece2 (1, [2,1,3]))
#print (pertenece2 (5, [1,2,3,5,4])) 

def pertenece3 (e:int, s:List [int]) -> bool:
    mi_numero : int = e
    mi_lista : List = s
    return mi_numero in mi_lista

#print (pertenece3 (1,[2,1,3]))
#print (pertenece3 (5,[2,1,3])) 
 

def pertenece4 (e:int, s:List [int]) -> bool:
    mi_numero : int = e
    mi_lista : List = s
    x : int = 0
    while x < len(mi_lista):
        if mi_lista[x] != mi_numero:
            x += 1
        else : return True
    return False

#print (pertenece4 (1, [2,3,1,4,6]))
#print (pertenece4 (3, [1,1,1,1])) 


# 2)

def divide_a_todos (s: List [int], e: int) -> bool:
    lista : List = s
    numero : int = e
    contador : int = 0
    for i in range (len(lista)):
        if lista[i] % numero == 0:
            contador += 1
    if contador == len(lista): return True
    else : return False
    

#print(divide_a_todos([3,6,9],3))
#print(divide_a_todos([3,6,9],2))
      
    
'''
for i in [1,2]:
    print (i)
    '''
    
def divide_a_todosV2 (s: List[int], e:int) -> bool:
    lista: List = s
    numero: int = e
    res: bool = True
    i: int = 0
    while (i < len(lista)) and (res == True):
        if lista[i] % numero != 0:
            res = False
        else:
            i += 1
    return res 

            
#print(divide_a_todosV2([3,6,9],3))
#print(divide_a_todosV2([3,6,9],2))    
           
def divide_a_todosV3 (s: List[int], e:int) -> bool:
    lista: List = s
    numero: int = e
    res: bool = True
    i: int = 0
    while (i < len(lista)):
        if lista[i] % numero != 0:
            res = False
            break
        else:
            i += 1
    return res    

#print(divide_a_todosV3([3,6,9],3))
#print(divide_a_todosV3([3,6,9],2)) 
#print (10%3)
#print (3%10)   


# 3)

def suma_total (s: List[int]) -> int:
    lista: List = s
    mi_suma : int = 0
    for i in range (len(lista)):
        mi_suma += lista[i]
    return mi_suma
'''
print (suma_total([1,2,3]))
print (suma_total([]))
print (suma_total([1,2,(-4)]))
print (suma_total([5,5,5,5,5]))
'''
       
def suma_totalV2 (s:List [int]) -> int:
    lista: List = s
    mi_suma: int = 0
    i : int = 0
    while i < len(lista):
        mi_suma += lista[i]
        i += 1
    return mi_suma 
'''
print (suma_totalV2([1,2,3]))
print (suma_totalV2([]))
print (suma_totalV2([1,2,(-4)]))
print (suma_totalV2([5,5,5,5,5]))
'''

# 4)

def maximo (s:List [int]) -> int:
    lista:List = s
    res: int = 0
    i : int = 0
    while (i < len(lista)):
        if lista [i] > res: res = lista[i]
        i += 1
    return res

#print (maximo([1,2,3]))
#print (maximo([1,2,3,9999]))
#print (maximo([1,2,(-3)]))

def maximoV2 (s:List [int]) -> int:
    lista: List = s
    res: int = 0
    for i in range (len(lista)):
        if lista[i] > res : res = lista[i]
    return res 

#print (maximoV2([1,2,3]))
#print (maximoV2([1,2,3,9999]))
#print (maximoV2([1,2,(-3)]))

# 5)

def minimo (s:List [int]) -> int:
    lista:List = s
    res: int = lista[0]
    i : int = 0
    while (i < len(lista)):
        if lista [i] < res: res = lista[i]
        i += 1
    return res

#print (minimo([1,2,3]))
#print (minimo([1,2,3,9999]))
#print (minimo([1,2,(-3)]))

def minimoV2 (s:List [int]) -> int:
    lista: List = s
    res: int = lista[0]
    for i in range (len(lista)):
        if lista[i] < res : res = lista[i]
    return res 

#print (minimoV2([1,2,3]))
#print (minimoV2([1,2,3,9999]))
#print (minimoV2([1,2,(-3)]))


#print (min([1,2,(-3)]))

# 6)

def ordenados (s:List[int]) -> bool:
    lista:List[int] = s
    res : bool = True
    i:int = 0
    contador:int = 0
    while (i < len (lista)) and (contador != len(lista)-1): # De esta forma cuando llega al último elemento ya no compara con nada más
        if lista[i] < lista [i+1]:                          # Hace la iteración la cantidad de veces necesarias 
            i += 1
            contador += 1
        else:
            res = False
            break 
    return res 
             
            
#print (ordenados ([1,2,3,98]))
#print (ordenados ([1,2,3,4,5,6,7,8,9,10,11,12,13,15,6666666,(-1)]))

# Otra forma que resuelve el problema que tenía:

def estanOrdenadosV2 (l:list) -> bool:
    res: bool = True
    i: int = 1
    while ((i<len(l)) & (res==True)):
        if (l[i-1] > l[i]):
            res = False
        print (i)
        i+=1
    return res

# 7) 

def pos_maximo (s:List[int]) -> int:
    lista:List[int] = s
    x :int = 0
    if len (lista) == 0:
        x = -1
    else:
        for i in range (len(lista)):
            if lista [i] == maximo (lista): # si el elemento en esa pos es igual al maximo de la lista el valor de x pasa a ser ese elemento
                x = i                      
                break                       # de esta forma me va a devolver el primero
    return x

#print (pos_maximo([3,4,5,6,2,1]))
#print (pos_maximo([]))
#print (pos_maximo([1,2,3,2,1,3,2,1]))

# 8)

def pos_minimo (s:List[int]) -> int:
    lista:List[int] = s
    x :int = 0
    if len (lista) == 0:
        x = -1
    else:
        for i in range (len(lista)):
            if lista [i] == minimo (lista): # Si el elemento en esa pos es igual al maximo de la lista el valor de x pasa a ser ese elemento
                x = i                       # Sin el break va a devolver el último
    return x

#print (pos_minimo([3,4,5,6,2,1]))
#print (pos_minimo([]))
#print (pos_minimo([1,2,3,2,1,3,2]))

# 9)


def longitud_mayor_7 (s:List[List[chr]]) -> bool:
    lista: List[List[chr]] = s
    res : bool = False
    for i in lista:
        if len(i) > 7:
            res = True
            break
    return res 
            
    
#print (longitud_mayor_7 (["mm","Delfinaaaaaa","hola"]))
#print (longitud_mayor_7 (["Da","hola"]))


# 10)

def palindromo (s: List[chr]) -> bool:
    lista : List [chr] = s
    if len(lista) == 0 or len(lista) == 1:
        return True
    else:
        return (lista == lista [::-1])
    
'''     
print (palindromo (["delfina"]))
print (palindromo (["abcba"]))
print (palindromo (["a"]))
print (palindromo ([""]))
'''



# 11)

def numeros_consecutivos (s: List [int]) -> bool:
    lista: List [int] = s
    contador : int = 0 
    i : int = 1
    while i < len(lista) and contador != 3:
        if lista[i-1] == lista [i]:
            contador += 1
        else:
            contador = 0
        i +=1
    if contador == 3:
        return True
    else : return False
    
print (numeros_consecutivos ([1,2,3,4])) #False
print (numeros_consecutivos ([1,2,2,2,3,4])) #True
print (numeros_consecutivos ([1,2,3,4,1,1])) #False
print (numeros_consecutivos ([1,2,3,7,6,7,4,3,7,4])) #False
