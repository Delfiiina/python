from queue import Queue as Cola
"""
1) Alerta Enfermedades Infecciosas (3 puntos)

Necesitamos detectar la aparición de posibles epidemias. 
Para esto contamos con un lista de enfermedades infecciosas y 
los registros de atención por guardia dados por una lista expedientes. 
Cada expediente es una tupla con ID paciente y enfermedad que motivó la atención. 
Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y 
su valor es la proporción de pacientes que se atendieron por esa enfermedad. 
En este diccionario deben aparecer solo aquellas enfermedades infecciosas cuya proporción supere cierto umbral.

problema alarma_epidemiologica (registros: seq⟨ZxString⟩, infecciosas: seq⟨String⟩, umbral: R) : dict⟨String,R⟩ {
  requiere: {0 < umbral < 1}
  asegura: {claves de res pertenecen a infecciosas}
  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de
  pacientes que se atendieron por esa enfermedad sobre el total de registros es mayor o igual al umbral,
  entonces res[enfermedad] = porcentaje}
  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de e pacientes que se atendieron
  
  por esa enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res}
}

2) Orden de atención (1 punto)

Desde el Hospital Fernandez nos pidieron solucionar una serie de problemas relacionados
con la información que maneja sobre los pacientes y el personal de salud. 
En primer lugar debemos resolver en qué orden se deben atender los pacientes que llegan a la guardia.
En enfermería, hay una primera instancia que clasifica en dos colas a los pacientes: una urgente y otra postergable 
(esto se llama hacer triage). A partir de dichas colas que contienen la identificación del paciente, 
se pide devolver una nueva cola según la siguiente especificación.

problema orden_de_atencion ( in urgentes: cola⟨Z⟩, in postergables: cola⟨Z⟩) : cola⟨Z⟩ {
  requiere: {no hay elementos repetidos en urgentes}
  requiere: {no hay elementos repetidos en postergables}
  requiere: {la intersección entre postergables y urgentes es vacía}
  requiere: {|postergables| = |urgentes|}
  asegura: {no hay repetidos en res }
  asegura: {res es permutación de la concatenación de urgentes y postergables}
  asegura: {Si urgentes no es vacía, en tope de res hay un elemento de urgentes}
  asegura: {En res no hay dos seguidos de urgentes}
  asegura: {En res no hay dos seguidos de postergables}
  asegura: {Para todo c1 y c2 de tipo "urgente" pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces c1 aparece antes que c2 en res}
  asegura: {Para todo c1 y c2 de tipo "postergable" pertenecientes a postergables si c1 aparece antes que c2 en postergables entonces c1 aparece antes que c2 en res}

3) Camas ocupadas en el hospital (2 puntos)
Queremos saber qué porcentaje de ocupación de camas hay en el hospital. 
El hospital se representa por una matriz en donde las filas son los pisos,
y las columnas son las camas. Los valores de la matriz son booleanos que indican si la cama está ocupada o no.
Si el valor es verdadero (True) indica que la cama está ocupada. 
Se nos pide programar en Python una función que devuelve una secuencia de enteros, indicando la proporción de camas ocupadas en cada piso.

problema nivel_de_ocupacion(camas_por_piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
  requiere: {Todos los pisos tienen la misma cantidad de camas.}
  requiere: {Hay por lo menos 1 piso en el hospital.}
  requiere: {Hay por lo menos una cama por piso.}
  asegura: {|res| = |camas|}
  asegura: {Para todo 0<= i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el total de camas del piso i)}
}

4) Quiénes trabajaron más? (2 puntos)
Dado un diccionario con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y
el valor es una lista de las horas trabajadas por día, queremos saber quienes trabajaron más para darles un premio.
Se deberá buscar la o las claves para la cual se tiene el máximo valor de cantidad total de horas, y devolverlas en una lista.

problema empleados_del_mes(horas:dicc⟨Z,seq⟨Z⟩⟩) : seq⟨Z⟩ {
  requiere: {No hay valores en horas que sean listas vacías}
  asegura: {Si ID pertence a res entonces ID pertence a las claves de horas}
  asegura: {Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos los otros IDs}
  asegura: {Para todo ID de claves de horas, si la suma de sus valores es el máximo de la suma de elementos de horas de los otros IDs, entonces ID pertences a res}
}
}
"""
# Ejercicio 1

def pertenece (enfermedad:str, infecciosas: list[str]) -> bool:
  for infecciosa in infecciosas:
    if infecciosa == enfermedad:
      return True
  return False

def contar_enfermedad (enfermedad: str, registros: list[tuple[int,str]]) -> int:
  contador : int = 0
  for tupla in registros:
    if tupla[1] == enfermedad:
      contador += 1
  return contador

########################################################################################################
#print (contar_enfermedad("c",[(1,"b"),(2,"b"),(3,"f"),(4,"a"),(5,"c"),(6,"c"),(7,"b"),(8,"y"),(9,"b")]))
########################################################################################################

def calcular_proporcion (a:int, b:int) -> float:
  return a/b


def alarma_epidemiologica (registros: list[tuple[int,str]], infecciosas: list[str], umbral: float) -> dict[str,float]:
  diccionario : dict[str,float] = {}
  
  for expediente in registros:
    if not pertenece(expediente[1],diccionario.keys()):
      proporcion : float = calcular_proporcion (contar_enfermedad(expediente[1],registros),len(registros))
      if pertenece(expediente[1],infecciosas) and (proporcion >= umbral):
        diccionario[expediente[1]] = proporcion
        
  return diccionario

###############################################################################################

#infecciosas = ["a","b","c","f"]
#registros = [(1,"b"),(2,"b"),(3,"f"),(4,"a"),(5,"c"),(6,"c"),(7,"b"),(8,"y"),(9,"b"),(10,"c"),(11,"c")]
#umbral = 0.01

#print (alarma_epidemiologica(registros,infecciosas,umbral))

###############################################################################################

# Ejercicio 2

def orden_de_atencion (urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
  res : Cola[int] = Cola()
  urgentes_aux : Cola[int] = Cola()
  postergables_aux : Cola[int] = Cola()
  
  if urgentes.empty():
    elem : int = postergables.get()
    postergables_aux.put(elem)
    res.put(elem)
    while not postergables_aux.empty():
      elem = postergables_aux.get()
      postergables.put(elem)
  else:
    while not urgentes.empty():
      caso_urgente : int = urgentes.get()
      urgentes_aux.put(caso_urgente)
      res.put(caso_urgente)
      caso_postergable : int = postergables.get()
      postergables_aux.put(caso_postergable)
      res.put(caso_postergable)
    
    while not postergables_aux.empty():
      elem = postergables_aux.get()
      postergables.put(elem)
      
    while not urgentes_aux.empty():
      elem =urgentes_aux.get()
      urgentes.put(elem)   
  
  return res
      
      
####################################################################
'''
urgentes = Cola()
urgentes.put(1)
urgentes.put(1)
urgentes.put(1)
postergables = Cola()
postergables.put(2)
postergables.put(2)
postergables.put(2)

print ("URGENTES ORIGINAL:")
print (urgentes.queue)
print ("POSTERGABLES ORIGINAL:")
print (postergables.queue)
print ("ORDEN DE ATENCION:")
print (orden_de_atencion(urgentes,postergables).queue)
# Tendria que quedar : [1,2,1,2,1,2] y el primero q sale es el 1
print ("URGENTES DESP: ESPERO [1,1,1]")
print (urgentes.queue)
print ("POSTERGABLES DESP: ESPERO [2,2,2]")
print (postergables.queue)
print ("EL PRIMERO Q SALE: ESPERO 1")
print (orden_de_atencion(urgentes,postergables).get())
'''
###################################################################

# Ejercicio 3

def cantidad_de_True (l:list[bool]) -> int:
  contador : int = 0
  for booleano in l:
    if booleano == True:
      contador += 1
  return contador 

def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
  res : list [float] = []
  
  for piso in camas_por_piso:
    res.append(cantidad_de_True(piso)/len(piso))
  return res

######################################################################

#camas_por_piso = [[True,False,False],[True,True,True],[False,False,False],[True,False,True]]
#print (nivel_de_ocupacion(camas_por_piso))

#######################################################################

    
