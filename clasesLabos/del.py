from queue import LifoQueue as Pila, Queue as Cola
from typing import List, TextIO

# Ej 6

def separar_string (string:str) -> list[str]:
    respuesta: list[str] = []
    guardado: str = ""

    for caracter in string:
        if caracter != " ":
            guardado += caracter
        else:
            respuesta.append(guardado)
            guardado = ""

    return respuesta

# (separar_string("1 1 + 2 *"))


def hacer_cuenta (s: str, m:str, a: str) -> float:
    elemento1 : float = float(s)
    elemento2 : float = float(m)
    res : float = 0

    if a == "+":
        res = elemento1 + elemento2
    elif a == "-":
        res = elemento2 - elemento1
    elif a == "*":
        res = elemento1 * elemento2
    else:        
        res = elemento2 / elemento1
    
    return res 


def evaluar_expresion (s: str) -> float:
    operandos : Pila = Pila()
    operadores : Pila = Pila ()
    expresion : list[str] = separar_string(s)

    for caracter in expresion: 
        if operadores.empty(): 
            if caracter not in ['+','-','*','/']:
                operandos.put (caracter)
            else:
                operadores.put(caracter)
                elemento1 : str = operandos.get()
                elemento2 : str = operandos.get()
                calculo: float = hacer_cuenta(elemento1,elemento2,caracter)
                operandos.put(calculo)


    return operandos.get()
            

print (evaluar_expresion("1 1 + 5 * 3 + 7 /")) # 1.857142
print (evaluar_expresion("1 6 + 8 * 2 /")) #25
print (evaluar_expresion("13 56 + 23 /")) #3


# Ejercicio 7
#Implementar una funci´on que dadas dos pilas de igual longitud devuelve una nueva pila con los elementos inter-
#calados. intercalar(p1:Pila, p2:Pila)->Pila. El tope de la pila resultado ser´a el tope de la p2. Nota: Ojo que hay que
#recorrer dos veces para que queden en el orden apropiado al final.
#def intercalar (p1:Pila, p2:Pila) -> Pila:
