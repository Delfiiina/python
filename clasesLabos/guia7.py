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
'''  
print (numeros_consecutivos ([1,2,3,4])) #False
print (numeros_consecutivos ([1,2,2,2,3,4])) #True
print (numeros_consecutivos ([1,2,3,4,1,1])) #False
print (numeros_consecutivos ([1,2,3,7,6,7,4,3,7,4])) #False
'''


# Labo
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

def ej13 (s:list[int]) -> int:
    lista1 : list[int] = []
    lista2 : list[int] = []
    indice1: int = 0
    indice2: int = 0
    for i in range (len(s)-1):
        if s[i] <= s [i+1]:
            lista1.append(s[i]) 
            lista1.append(s[i+1])
            indice1 = i
        else:
            lista1.append(s[i])
            lista2.append(s[i+1])
            indice1 = i
            indice2 = i+1

# 14)

# Al final esta no la necesité
def cant_digitos_numero (numero:int) -> int:
    respuesta: int = 0
    if numero == 0:
        return 1
    while numero > 0:
        numero = numero // 10
        respuesta += 1
    return respuesta

#print (cant_digitos_numero(0))


def digitos_de_numero (numero:int) -> list[int]:
    respuesta: list[int] = []
    if numero == 0 :
        return [0]
    while numero >0:
        respuesta.append (numero % 10)
        numero = numero // 10
    return respuesta

#print (digitos_de_numero (123456789123456789))

def cantidad_digitos_impares (s: list[int]) -> int:
    respuesta : list [int] = []
    for i in range (len(s)):
        for digito in digitos_de_numero(s[i]):
            if digito % 2 == 1:
                respuesta.append(digito)
    return len(respuesta)

#print(cantidad_digitos_impares ([467777,235583,82,246]))


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

# 3)

def sin_vocales (s:list[str]) -> list[str]:
    vocales : list [str] = ['a','e','i','o','u','A','E','I','O','U']
    respuesta : list [str] = []
    for letra in s:
        if pertenece2 (letra,vocales) == False:  # le puedo pasar a pertenece un str y una lista de str 
            respuesta.append(letra)
    return respuesta 

#print (sin_vocales(["z","a","e","i","o","b","c"]))
#print (pertenece3 ("e", ['a','e','i','o','u','A','E','I','O','U']))    

# HAY UN ERROR EN MI FUNCIÓN PERTENECE (LA 1)  

# 4)

def reemplaza_vocales (s:list[str]) -> list[str]:
    respuesta : list[str] = []
    vocales : list [str] = ['a','e','i','o','u','A','E','I','O','U']
    if s == [] :
        return []
    for letra in s:
        if pertenece2 (letra,vocales) == False:
            respuesta.append(letra)
        else:
            respuesta.append("-")
    return respuesta
#   return ''.join(respuesta)

'''
print (reemplaza_vocales(["a","b","e","g","I","i","i","p"]))
print (reemplaza_vocales(["g","b","v","g","n","m","l","p"]))
print (reemplaza_vocales([]))
print (reemplaza_vocales(["p"]))
print (reemplaza_vocales(["a"]))
print (reemplaza_vocales("hola"))
'''


# 5)

def da_vuelta_str (s: list[str]) -> list[str]:
    respuesta :list [str] = []
    for i in range (len(s)):
        respuesta.append (s[len(s)-i-1])
    return respuesta

'''
print (da_vuelta_str("hola"))
print (da_vuelta_str("abcdefghijklmn"))
print (da_vuelta_str("")) 
'''

# 6)

def eliminar_repetidos (s: list [str]) -> list [str]:
    respuesta : list [str] = []
    for i in range (len(s)):
        if pertenece2 (s[i],respuesta) == False:
            respuesta.append(s[i])
    return respuesta 

'''
print (eliminar_repetidos("holaaaaaaoma"))
print (eliminar_repetidos(""))
print (eliminar_repetidos("hola"))
print (eliminar_repetidos("mmdmdmdmdddmdmdmdddmdmdmdddmddmmdmdd"))
print (eliminar_repetidos("aaaaaaaaaaaaaaaaaaaaaaaaaaa"))
'''


# Ejercicio 3

def promedio (notas: list [int]) -> float:
    suma : int = 0
    for nota in notas:
        suma += nota
    return suma / len (notas)
      
def todas_mayores_4 (notas:list[int]) -> bool:
    res: bool = True
    for i in range (len(notas)):
        if notas[i] < 4:
            res = False
            break
        else:
            continue
    return res
     
'''''
print (todas_mayores_4([1,2,6]))
print (todas_mayores_4([5,5,5]))
print (todas_mayores_4([8,8,8,8,8,8]))
print (todas_mayores_4([1]))
print (todas_mayores_4([6,1]))
print (todas_mayores_4([1,6]))

'''''

def resultadoMateria (notas: list [int]) -> int:
    res:int = 0
    if todas_mayores_4(notas) == True:
        if promedio (notas) >= 7:
            return 1
        else: 
            return 2
    else:
        return 3
        
'''''
print (resultadoMateria([1,7,7,7,7])) #3
print (resultadoMateria([7,7,7,7])) #1
print (resultadoMateria([1,7,7,7,7,9,9,9,9,9])) #3
print (resultadoMateria([6,6,6,6,6])) #2
print (resultadoMateria([1,7,7,7,7,1,1,1,1,1,1,1,1])) #3
print (resultadoMateria([2,3,4])) #3
print (resultadoMateria([10,10,10,9,8,7,6,5,4])) #1
'''

# Ejercicio 4

def cuenta_bancaria (historial: list[(str,int)]) -> int:
    saldo: int = 0
    for movimiento in historial:
        if movimiento[0] == "I":
            saldo += movimiento[1]
        else:
            saldo -= movimiento[1]
    return saldo 
'''''
print (cuenta_bancaria([("I",10),("I",20),("R",5),("I",20),("R",10)]))
print (cuenta_bancaria([("I",10)]))
print (cuenta_bancaria([("R",5)]))
print (cuenta_bancaria([]))
'''


# Ejercicio 5
# 1)
# Pregunta de variable global
def pertenece_a_cada_uno_version_1 (s:list[list[int]], e:int, res: list[bool]):
    for lista in s:
        res.append(pertenece2(e,lista))
'''''
lista: list[bool] = [True,False]
print (lista)
print(pertenece_a_cada_uno_version_1([[1,2],[1],[2,3]],1,lista))
print (lista)
print(pertenece_a_cada_uno_version_1([[1,2],[1],[2,3]],2,lista))
print (lista)
print(pertenece_a_cada_uno_version_1([[1,2,5],[1,5],[2,3],[],[12,13,6],[5]],5,lista))
print (lista)
'''

# 2)
def pertenece_a_cada_uno_version_2 (s:list[list[int]], e:int, res: list[bool]):
    res: list[bool] = []
    for lista in s:
        res.append(pertenece2(e,lista))
        

# 3) 
def pertenece_a_cada_uno_version_3 (s:list[list[int]], e:int) -> list[bool]:
    res: list[bool] = []
    for lista in s:
        res.append(pertenece2(e,lista))
    
    
# Ejercicio 6
# 1)

def es_matriz (s: list[list[int]]) -> bool:
    largo_que_vale: int = len (s[0])
    for i in range (len (s)):
        return (len(s[i]) == largo_que_vale)

'''''   
print (es_matriz([[1,2],[3,4],[5,6]]))
print (es_matriz([[1,2,3],[3,4],[5,6]]))
print (es_matriz([[1,2],[3,4,4],[5,6]]))
print (es_matriz([[1,2],[3,4],[5,6,8]]))
print (es_matriz([[1,2],[3,4,10],[11,11,5,6]]))
'''


def es_matriz (s:list[list[int]]) -> bool:
    tamano: int = len(s[0])
    res : bool = True
    if tamano == 0:
        res = False
    else:
        contador : int = 1
        while res == True and contador < len(s):
            for i in range (1,len(s)):
                if len (s[i]) != tamano:
                    res = False
            contador += 1        
    return res 


'''''
print (es_matriz([[0,1,2],[3,4,5],[5,6,7]])) #True
print (es_matriz([[],[2,3]])) #False
print (es_matriz([[3,2,1],[5,6],[2,7,8]])) #False
print (es_matriz([[8,9],[]])) # False
print (es_matriz([[1,1,1,1,1,1,1]])) #True
'''


def ordenados (s:list[int]) -> bool:
    if len(s) == 0:
        return True
    culo : int = s[0]
    res : bool = True
    contador : int = 1
    while res == True and contador < len(s):
        for i in range (1,len(s)):
            if s[i] > culo: 
                culo = s[i]
                contador += 1
            else:
                res = False
    return res
'''''
print (ordenados ([1,2,3])) # T
#print (ordenados ([5,2])) # F
#print (ordenados ([])) # T
#print (ordenados([1,1,1,1]))
print (ordenados([1,4,9,56789]))
#print (ordenados([7])) #T
'''


def filas_ordenadas (m:list[list[int]], res :list[bool]) -> None:
    if len(m[0]) == 0:
        res= [True]
    res = []
    for i in range (len(m)):
        res.append(ordenados(m[i]))
    print (res)

#filas_ordenadas([[1,2,3],[5,6,8],[3,2,4],[6,6,6],[(-1),0,3]],[True])   



def columna (m:list[list[int]], e: int) -> list[int]:
    res : list[int] = []
    for i in range (len(m)):
        res.append (m[i][e])
    return res

'''''
print (columna([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],0))
print (columna([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],2))
print (columna([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],1))
'''


def columnas_ordenadas (m:list[list[int]]) -> list[bool]:
    res: list [bool] = []
    for i in range (len(m[0])):
        res.append(ordenados(columna(m,i)))
    return res
 
'''''
print (columnas_ordenadas([[1,1,1],[2,2,2],[3,3,3]])) 
print (columnas_ordenadas([[1,5,1],[2,2,2],[3,3,3]]))
print (columnas_ordenadas([[1,1,1],[8,2,2],[3,3,3]]))
print (columnas_ordenadas([[1,1,1],[2,2,2],[3,3,(-5)]]))
'''


def transponer (m:list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []
    for i in range (len(m[0])):
        res.append (columna(m,i))
    return res

#print (transponer([[1,2,3],[4,5,6],[7,8,9]]))


def fAux (m:list[list[str]]) -> int:
    if "X" == m[0][0] == m[0][1] == m[0][2]:
        return 1
    elif "O" == m[0][0] == m[0][1] == m[0][2]:
        return 0
    elif "X" == m[1][0] == m[1][1] == m[1][2]:
        return 1
    elif "O" == m[1][0] == m[1][1] == m[1][2]:
        return 0
    elif "X" == m[2][0] == m[2][1] == m[2][2]:
        return 1
    elif "O" == m[2][0] == m[2][1] == m[2][2]:
        return 0
    else:
        return 2


def fAux2 (m:list[list[str]]) -> int:
    if m[0][0] == m[1][1] == m[2][2] == "X":
        return 1
    elif m[0][2] == m[1][1] == m[2][0] == "O":
        return 0
    else:
        return 2


def quien_gana_tateti (m:list[list[int]]) -> int:
    res: int = 2
    if fAux (m) != 2:
        return (fAux(m))
    elif fAux (transponer(m)) != 2:
        return fAux (transponer(m))
    elif fAux2 (m) != 2:
        return (fAux2(m))
    return 2


#print (quien_gana_tateti([["O","X","O"],["X","X","O"],["O","X","X"]]))

# Ejercicio 7
# 1) en ambas falla si en vez de ingresar un nombre apreto enter 

def lista_con_nombre () -> list[str]:
    mi_lista: list[str] = []
    nombre_estudiante: str = input ("Ingresar nombre de estudiante: ")
    
    while nombre_estudiante != "listo" or "":
        mi_lista.append(nombre_estudiante)
        nombre_estudiante = input ("Ingresar nombre de estudiante: ")
        
    print(mi_lista) 
       
#lista_con_nombre()
          
 
def lista_con_nombre2 () -> list[str]:
    mi_lista: list[str] = []
    nombre_estudiante: str = input ("Ingresar nombre de estudiante: ")
    
    while nombre_estudiante != "listo" or "":
        mi_lista.append(nombre_estudiante)
        nombre_estudiante = input ("Ingresar nombre de estudiante: ")
        
    return(mi_lista)

  
#print(lista_con_nombre2())  

       
#2)          


def historial_monedero () -> list[tuple[str,float]]:
    historial: list[tuple[str,float]] = []
    dinero: float = 0
    paso_del_usuario: str = input ("Desea cargar crédito, descontar crédito o finalizar? ")
    
    while paso_del_usuario != "finalizar":
        if paso_del_usuario == "cargar crédito":
            cuanto: float = float(input ("Cuánto desea cargar? "))
            dinero += cuanto
            historial.append(["C",cuanto])
            historial.append (["Cargó dinero, actualmente tiene", dinero])
            paso_del_usuario: str = input ("Desea cargar crédito, descontar crédito o finalizar? ")
        
        else:
            cuanto = float(input ("Cuánto desea descontar? "))
            historial.append (["D",cuanto])
            dinero -= cuanto
            historial.append (["Descontó dinero, actualmente tiene", dinero])
            paso_del_usuario: str = input ("Desea cargar crédito, descontar crédito o finalizar? ")

    return historial
    
print (historial_monedero())
        
    
            
    