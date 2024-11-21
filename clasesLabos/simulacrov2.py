from queue import Queue as Cola

# Ejercicio 1

##############################################################

def pertenece (nombre:str, diccionario_keys:list[str]) -> bool:
    for elemento in diccionario_keys:
        if nombre == elemento:
            return True
    return False

##############################################################

def gestion_ventas (ventas_empleado_producto : list [tuple[str,str,int]]) -> dict [str,list[tuple[str,int]]]:
    diccionario : dict [str,list[tuple[str,int]]] = {}
    
    for tupla in ventas_empleado_producto:
        if pertenece (tupla[0] , diccionario.keys()) == False: 
            nombre : str = tupla[0]
            sus_ventas : list[tuple[str,int]] = []
            for ventas in ventas_empleado_producto:
                if ventas[0] == nombre:
                    tupla_de_nombre : tuple[str,int] = (ventas[1],ventas[2])
                    sus_ventas.append(tupla_de_nombre)
            diccionario[nombre] = sus_ventas
            nombre = ""
            sus_ventas = []
    
    return diccionario
                    
#prueba = [("Juan","pan",2),("Maria","jugo",4),("Pedro","limon",3),("Juan","jugo",5),("Malena","papel",1),("Malena","pan",2),("Maria","limon",4),("Juan","papel",2)]
#print (gestion_ventas(prueba))

# Ejercicio 2

def cantidad_digitos_impares (numeros:list[int]) -> int:
    res : list[int] = []
    
    for numero in numeros:
        while numero > 0:
            if (numero%10) % 2 != 0:
                res.append((numero%10))
            numero = numero // 10
     
    return len(res)

#print (cantidad_digitos_impares([26,13,111,0,268,9]))       
 
# Ejercicio 3

def reordenar_cola_primero_numerosas(carpetas: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:
    res : Cola[tuple[str,int]] = Cola()
    carpetas_aux : Cola[tuple[str,int]] = Cola()
    menor_igual_umbral : list [tuple[str,int]] = []
    mayores_umbral : list [tuple[str,int]] = []
    
    while not carpetas.empty():
        carpeta : tuple[str,int] = carpetas.get()
        carpetas_aux.put(carpeta)
        if carpeta[1] > umbral:
            mayores_umbral.append(carpeta)
        else:
            menor_igual_umbral.append(carpeta)
    
    for carpeta in mayores_umbral:
        res.put(carpeta)
    for carpeta in menor_igual_umbral:
        res.put(carpeta)
        
    while not carpetas_aux.empty():
        carpeta : tuple[str,int] = carpetas_aux.get()
        carpetas.put(carpeta)
    
    return res

colaa = Cola()
colaa.put(("a",6))
colaa.put(("b",1))
colaa.put(("c",4))
colaa.put(("d",10))
colaa.put(("e",8))
colaa.put(("f",1))

# RTA ESPERADA ([('a', 6), ('d', 10), ('e', 8), ('b', 1), ('c', 4), ('f', 1)])
#print (colaa.queue)
#print (reordenar_cola_primero_numerosas(colaa,5).queue)
#print (colaa.queue)

# Ejercicio 4
    
def esta_ordenada_decreciente (l:list[int]) -> bool:
    

def matriz_cuasi_decreciente(matriz: list[list[int]]) -> bool: