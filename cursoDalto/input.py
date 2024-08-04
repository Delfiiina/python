# Pedirle al usuario un nombre
nombre = input ("Escribir tu nombre: ")
print (f"Hola {nombre}")    #LO COMENTO PQ MOLESTA EN LA TERMINAL

# Pedirle al usuario un número
# Ejemplo de un error
numero = input ("Escribir un número: ")
#respuesta = numero * 2
#print (respuesta)
# devuelve 1010 y no 20
# para arregarlo entonces usamos la función int
#respuesta2 = int(numero) * 2
#print (respuesta2)
respuesta3 = float (numero) * 2
print (f"Ese número multiplicado por dos es {respuesta3}")
