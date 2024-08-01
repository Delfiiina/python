print ("Hola mundo")

# VARIABLES

a = 15
b = 8
c = a + b
print (c)

nombre = "Delfina"
print (nombre)
  
numero = 10
numero += 1
print (numero)
 
bienvenida = "Hola " + nombre + " ¿Cómo estás?"
print (bienvenida)

bienvenida2 = f"Hola {numero} ¿cómo estás?"
print (bienvenida2)

# ejemplo de un dato que se borra:
# nombre = "Delfina"
# del nombre
#  print (nombre) --> error

# ejemplo de un dato que no se borra dado que se borra luego de la función
numero2 = 20
cuenta = numero2 * 5 
del numero2
print (cuenta)

print ("ola" in bienvenida)
print ("Pedro" in bienvenida)

# definiendo una variable con snake_case
nombre_completo_tuyo = "Delfina Boyadjian Varde"


# Datos compuestos
lista = ["primero",2,False]
print (lista)
print (lista [2])
tupla = ("primero",2,False)

# modificando una lista (la tupla NO se puede modificar)
lista [1] = 3
print (lista)

conjunto = {"primero",2,False}  # no se puede modificar tampoco
print (conjunto) 
# print (conjunto [1]) no se puede 
# conjunto = {"primero","primero"} no se pueden repetir datos, en las listas y en las tuplas si

diccionario = {
    'nombre' : "Delfina",
    'edad' : 19,
    'pelo_negro' : False
}
print (diccionario)
print (diccionario ['edad'])
