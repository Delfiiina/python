from typing import List, Dict, Tuple

# Ejercicio 1
# 1

def pertenece (numero:int, lista:List[int]) -> bool:
    i: int = 0
    mi_numero : int = numero
    mi_lista : List = lista
    if mi_numero == mi_lista [i] : 
        return True 
        i += 1
    else :
        return False

print (pertenece (5, [1,2,3]))
    