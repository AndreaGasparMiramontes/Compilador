import lexico
from pila import Pila

##    | id |  + |  $ |  E |
##  0 | d2 |    |    |  1 |
##  1 |    |    | r0 |    |
##  2 |    | d3 | r2 |    |
##  3 | d2 |    |    |  4 |
##  4 |    |    | r1 |    |

estado = 0

pila = Pila()

texto = input("Introduce el texto a analizar: ")
elementos = lexico.analizador(texto)
e = False
accepted = False
pila.push(0)
print(pila)
a = 0
while(not accepted):
    estado = pila.top()
    if estado == "E":
        pila.pop()
        e = True
        estado = pila.top()
    print("Lexema: ",elementos[a]['lexema'],"Token: ",elementos[a]['token'],"num: ",elementos[a]['num'])
    if estado == 0:
        if e:
            pila.push("E")
            pila.push(1)
            e = False
        elif elementos[a]['token'] == "id":
            pila.push(elementos[a]['num'])
            pila.push(2)
            a+=1
        
    if estado == 1:
        if elementos[a]['token'] == "pesos":
            print("Cadena aceptada")
            accepted = True
    if estado == 2:
        if elementos[a]['token'] == "OpSuma":
            pila.push(elementos[a]['num'])
            pila.push(3)
            a+=1
        elif elementos[a]['token'] == "pesos":
            pila.pop()
            pila.pop()
            pila.push("E")
    if estado == 3:
        if e:
            pila.push("E")
            pila.push(4)
            e = False
        elif elementos[a]['token'] == "id":
            pila.push(elementos[a]['num'])
            pila.push(2)
            a+=1
        
    if estado == 4:
        if elementos[a]['token'] == "pesos":
            pila.pop()
            pila.pop()
            pila.pop()
            pila.pop()
            pila.pop()
            pila.pop()
            pila.push("E")

    print(pila)




