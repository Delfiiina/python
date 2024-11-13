from queue import Queue as Cola

# Ejercicio 1
def pertenece (e:str, lista:list[str]) -> bool:
    
    for persona in lista:
        if e == persona:
            return True
    return False
     
def gestion_ventas(ventas_empleado_producto: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
    diccionario : dict[str, list[tuple[str,int]]] = {}
    
    for tupla in ventas_empleado_producto:
        empleado: str = tupla[0]
        info = (tupla[1],tupla[2])
        if not pertenece (empleado, diccionario.keys()):
            diccionario [empleado] = [info]
        else:
            diccionario [empleado].append(info)
    
    return diccionario
      
# Ejercicio 2

def cantidad_digitos_impares(numeros: list[int]) -> int:
    res : list [int] = []
    
    for elemento in numeros:
        elemento_str : str = str(elemento)
        for caracter in elemento_str:
            caracter_int : int = int (caracter)
            if caracter_int % 2 != 0:
                res.append(caracter_int)
    
    return len(res)

#print (cantidad_digitos_impares([2468,812,246]))

# Ejercicio 3
def reordenar_cola_primero_numerosas(carpetas: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:
    cola_abajo_umbral : Cola [tuple[str,int]] = Cola()
    cola_arriba_umbral : Cola [tuple[str,int]] = Cola()
    lista_de_cosas: Cola [tuple[str,int]] = Cola ()
    res : Cola[tuple[str,int]] = Cola ()
    
    while not carpetas.empty():
        carpeta : tuple[str,int] = carpetas.get()
        lista_de_cosas.put(carpeta)
        if carpeta[1] > umbral:
            cola_arriba_umbral.put(carpeta)
        else:
            cola_abajo_umbral.put(carpeta)
    
    while not lista_de_cosas.empty():
        carpetas.put(lista_de_cosas.get())
        if not cola_arriba_umbral.empty():
            res.put(cola_arriba_umbral.get())
        else:
            res.put(cola_abajo_umbral.get())

    return res
        
    
col = Cola()
col.put(("a",9))
col.put(("b",15))
col.put(("c",4))
col.put(("d",21))
# col = [("a",9),("b",15),("c",4),("d",21)]
print (col.queue)
print (reordenar_cola_primero_numerosas(col,10).queue)
print (col.queue)


# Ejercicio 4

def esta_ordenada_decreciente (l:list[int]) -> bool:
    
    for i in range (len(l)-1):
        if l[i] <= l[i+1]:
            return False
    return True       
    
def matriz_cuasi_decreciente(matriz: list[list[int]]) -> bool:
    lista_con_max : list [int] = []
    
    for elemento in matriz:
        maximo : int = elemento[0]
        for i in range (1,len(elemento)):
            if elemento[i] > maximo:
                maximo = elemento[i]
        lista_con_max.append (maximo)
        
    return esta_ordenada_decreciente(lista_con_max)
        
print (matriz_cuasi_decreciente([[13,14,15,16],[2,1,1,1],[5,6,7,8],[1,2,3,4]]))