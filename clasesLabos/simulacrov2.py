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
    
            