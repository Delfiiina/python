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
    
def divide_a_todosV2 (s: List, e:int) -> bool:
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
           
def divide_a_todosV3 (s: List, e:int) -> bool:
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

print(divide_a_todosV3([3,6,9],3))
print(divide_a_todosV3([3,6,9],2)) 
   
#  3)

