from typing import List

# 11)

def numeros_consecutivos (s: list [int]) -> bool:
    contador : int = 1
    i : int = 1
    while i < len(s) and contador != 3:
        if s[i-1] == s [i]:   # Si encuentra dos iguales, le suma 1 al contador (que estaría en 2)
            contador += 1
        else:
            contador = 1   # Cuando encuentra uno distinto vuelve el contador a 1
        i +=1
    return contador == 3

def numeros_consecutivos_v2 (s: list [int]) -> bool:
    for i in range(len(s)-2): 
        # s[i], s[i+1], s[i+2]
        if s[i]==s[i+1] and s[i+1]==s[i+2]: # Vas chequeando directamente de a 2
            return True
    return False
'''   
print (numeros_consecutivos ([1,2,3,4])) #False
print (numeros_consecutivos ([1,2,2,2,3,4])) #True
print (numeros_consecutivos ([1,2,3,4,1,1])) #False
print (numeros_consecutivos ([1,2,3,7,6,7,4,3,7,4])) #False
print (numeros_consecutivos ([1,1,1])) # True
print (numeros_consecutivos ([1,1])) # False

print (numeros_consecutivos_v2 ([1,2,3,4])) #False
print (numeros_consecutivos_v2 ([1,2,2,2,3,4])) #True
print (numeros_consecutivos_v2 ([1,2,3,4,1,1])) #False
print (numeros_consecutivos_v2 ([1,2,3,7,6,7,4,3,7,4])) #False
print (numeros_consecutivos_v2 ([1,1,1])) # True
print (numeros_consecutivos_v2 ([1,1])) # False
'''


# 12)

def pertenece2 (e:int, s:List [int]) -> bool:
    mi_numero : int = e
    mi_lista : List = s
    for i in range (0,len(mi_lista),1):
        if mi_lista[i] == mi_numero:
            return True 
    return False

def sacar_elemento (lista: list[str], letra: str) -> list[str]:
    nueva_lista: list[str] = []
    for i in range (len(lista)):
        if lista [i] != letra:
            nueva_lista.append(lista[i])
    return nueva_lista

#print (sacar_elemento(['h','o','l','a'],'o'))


def vocales_distintas (palabra: str) -> bool:
    vocales : list [str] = ['a','e','i','o','u','A','E','I','O','U']
    contador_vocales : int = 0
    for letra in palabra:
        if pertenece2 (letra,vocales) == True:
            contador_vocales += 1
            vocales = sacar_elemento (vocales, letra)
    return contador_vocales >= 3  


'''
print (vocales_distintas ("computadora")) # True
print (vocales_distintas ("aei")) # True
print (vocales_distintas ("ae")) # False
print (vocales_distintas ("lmpy")) # False
print (vocales_distintas ("eeeeeeeeeeee")) # False
print (vocales_distintas ("mmmmmmmaaa")) # False
print (vocales_distintas ("mmammanvnvanll")) # False
'''


# 13) Recorrer una seq⟨Z⟩ y devolver la posicion donde inicia la secuencia de numeros ordenada mas larga. Si hay dos
# subsecuencias de igual longitud devolver la posicion donde empieza la primera. La secuencia de entrada es no vacıa.


def largo_subseq (indice:int, secuencia: list [int]) -> int:
    largo: int = 0
    i: int = 0
    if i == indice:
        if secuencia[i] < secuencia[i+1]:
                largo += 1
                i += 1
        else:
            return largo
    else:
        i += 1

print (largo_subseq (3,[1,2,3,4,5,6,7])) # 4

# Ejercicio 2

# 1)

def ceros_en_pos_pares (s: list[int]) -> None:
    for i in range (len(s),2):
        s[i] = 0

# print (ceros_en_pos_pares([1,2,3,4,5]))

#2)

def ceros_en_pos_pares2 (s: list[int]) -> list[int]:
    lista : list[int] = s # esta mal pq la toma por referencia, entonces modifica también la lista original
    for i in range (0,len(lista),2):
        lista[i] = 0
    return lista 

def ceros_pos_pares2_bien (s:list [int]) -> list [int]:
    respuesta : list [int] = []
    for i in range (len(s)):
        if i % 2 == 0:
            respuesta.append(0)
        else:
            respuesta.append(s[i])
    return respuesta
