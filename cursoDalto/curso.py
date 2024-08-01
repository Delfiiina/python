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

 
