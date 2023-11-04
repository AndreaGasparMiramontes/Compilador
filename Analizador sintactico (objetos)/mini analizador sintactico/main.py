import lexico
from pila import Pila
from ep import EP

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
    input()
    estado = pila.top()
    if isinstance(estado, EP):
        e_cont = pila.pop()
        e = True
        estado = pila.top()
    #print("Lexema: ",elementos[a]['lexema'],"Token: ",elementos[a]['token'],"num: ",elementos[a]['num'])
    if estado == 0:
        if e:
            pila.push(e_cont)
            pila.push(1)
            e = False
        elif elementos[a]['token'] == "id":
            pila.push(elementos[a]['lexema'])
            pila.push(2)
            a+=1
        else:
            print("Cadena rechazada")
            accepted = True
        
    if estado == 1:
        if elementos[a]['token'] == "pesos":
            pila.pop()
            b = pila.pop()
            print("Cadena aceptada")
            print(b)
            accepted = True
        else:
            print("Cadena rechazada")
            accepted = True
    if estado == 2:
        if elementos[a]['token'] == "OpSuma":
            pila.push(elementos[a]['lexema'])
            pila.push(3)
            a+=1
        elif elementos[a]['token'] == "pesos":
            pila.pop() #num
            c = EP("E")
            c.id = pila.pop() #id
            pila.push(c)
        else:
            print("Cadena rechazada")
            accepted = True
    if estado == 3:
        if e:
            pila.push(e_cont)
            pila.push(4)
            e = False
        elif elementos[a]['token'] == "id":
            pila.push(elementos[a]['lexema'])
            pila.push(2)
            a+=1
        else:
            print("Cadena rechazada")
            accepted = True
        
    if estado == 4:
        if elementos[a]['token'] == "pesos":
            c = EP("E")
            pila.pop()
            c.E = pila.pop()
            pila.pop()
            c.mas = pila.pop()
            pila.pop()
            c.id = pila.pop()
            pila.push(c)
        else:
            print("Cadena rechazada")
            accepted = True
    print(pila)




