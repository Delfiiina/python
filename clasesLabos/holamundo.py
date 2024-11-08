from queue import LifoQueue as Pila

#[] 
# Ejercicio 6


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
    contador_operadores : int = 0
    vacio : str = ""

    for caracter in s:
        if caracter not in ["+","-","*","/"]:
            vacio += caracter
        elif caracter in ["+","-","*","/"]:
          operadores.put(caracter)   
          contador_operadores += 1
          if contador_operadores == 1:
            elemento1 : str = operandos.get()
            elemento2 : str = operandos.get()
            operador1 : str = operadores.get()
            calculo: float = hacer_cuenta(elemento1,elemento2,operador1)
            operandos.put(calculo)
            operadores = Pila ()
            contador_operadores = 0       
        elif caracter == " ":
            operandos.put(vacio)
            vacio = ""
    
    return operandos.get()


#print (evaluar_expresion("1 1 + 5 * 3 + 7 /"))
#print (evaluar_expresion("1 6 + 8 * 2 /"))
print (evaluar_expresion("13 56 + 23 /"))

