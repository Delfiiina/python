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
 