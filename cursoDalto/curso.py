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

# Operadores aritméticos
suma = 10 + 5
resta = 10 - 5
multiplicacion = 2 * 5
division = 10 / 5 # devuelve float
potencia = 2 ** 5
division_baja = 10 // 5
modulo = 10 % 5 
print (suma)
print (resta)
print (multiplicacion)
print (division)
print (potencia)
print (division_baja)
print (modulo)

tipo_de_dato = type (5) # type() nos devuelve que tipo de dato es 
print (tipo_de_dato)

# Operadores de comparación, devuelve o True o False
igual_que = 5 == 6 # devuelve False
distinto_de = 5 != 6 # devuelve True
mayor_que = 6 > 5
menor_que = 5 < 6
mayor_o_igual = 5 >= 7
menor_o_igual = 5 <= 5
print (igual_que)
print (distinto_de)
print (mayor_o_igual)
print (mayor_que)
print (menor_o_igual)
print (menor_que)

# Condicionales. Ir cambiando las variables definidas para ver cómo funciona

edad = 17
if edad >= 18:
    print ("Podes pasar")
else:
    print ("No podes pasar")

ingreso_mensual = 30

if ingreso_mensual > 80:
    print ("Bien")
elif ingreso_mensual >50:
    print ("Maso")
else:
    print ("Mal")

puntos_ganados = 290
puntos_perdidos = 45

if puntos_ganados > 300:
    if puntos_ganados - puntos_perdidos <= 150:
        print ("Podrias haber ganado")
    else:
        print ("Ganaste")
elif puntos_ganados > 150:
    if puntos_ganados - puntos_perdidos <= 150:
        print ("Podrias haber quedado segundo")
    else :
        print ("Casi")
else:
    print ("Perdiste")
    
resultado = True & True
resultado2 = False | True
resultado3 = not True
resultado4 = not False

print (resultado)
 
# MÉTODOS
# CADENAS

cadena1 = "Hola soy Delfi"
cadena2 = "bienvenido!"
cadena3 = "ME GUSTA EL CAFE"

#print (dir (cadena1))  # los comento pq molestan en la terminal 
#print (dir (4))
print (cadena1.upper())
print ("Tengo 19 años".upper())
print (cadena3.lower())
print (cadena2.capitalize())
print (cadena1.find("soy")) # pasa la posición
print (cadena1.index("a"))  # si no hay coincidencias tira un error
print (cadena2.isnumeric())
print ("3".isnumeric())  # Verifica que sea un número aunque este entre " " (lo cual, en definitiva, lo convierte en un texto)
print (cadena2.isalpha())  
print ("Hola".isalpha())
print (cadena1.count("soy"))
print (cadena1.count("z"))
print (cadena2.count("e"))
print (len(cadena2)) # Función
print (len("hola!"))
print (cadena1.startswith("c"))
print (cadena3.startswith("ME G"))
print (cadena1.endswith("jj"))
print (cadena2.endswith("!"))
print (cadena1.replace("Delfi","Marta"))
print (cadena2.replace("e","kakaka"))
print (cadena3.replace("bu","ba"))
cadena4 = "Hola,como,estás,todo,bien?"
print (cadena4.split(","))
print (cadena4.split(" "))
cadena5 = "Hola,como,estás,todo,bien?,,"
print (cadena5.split(","))
cadena6 = "Hola,como,estás,todo,bien?,    ,    "
print (cadena6.split(","))

# LISTAS
lista1 = [1,2,"Delfi",False,True]
print (list([1,2,"Delfi",False,True]))
print (len(lista1))
lista1.append("JAJA") # No imprime nada de por sí, me cambió la lista. Importa el orden con el q ponemos las cosas
print (lista1) # Ahora si se ve el nuevo elemento en la lista
lista1.insert(1,"Dos")
print (lista1)
lista1.extend([34,"caja",True])
print (lista1)
lista1.pop(0)
print (lista1)
lista1.pop (-1)
print (lista1)
lista1.remove("Delfi")
print (lista1)
#lista1.remove("sol") # Me va a tirar error ya que ese elemento no está en la lista
#lista1.clear()
#print (lista1)
lista2 = [14,6,False,22,876,True,34,9,5,5,True,False]
print (lista2)
lista2.sort()
print (lista2)
lista2.sort(reverse=True)
print (lista2)

print (lista1)
lista1.reverse()
print (lista1)

# TUPLAS
tupla1 = (1,2,1)
print (type(tupla1))
print (tupla1.index(2))
print (tupla1.count(1))

# DICCIONARIOS


