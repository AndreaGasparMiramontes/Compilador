import lexico
from pila import Pila
from ep import EP

pila = Pila()

##    | id |  + |  $ |  E |
##  0 | d2 |    |    |  1 |
##  1 |    |    | r0 |    |
##  2 |    | d3 | r2 |    |
##  3 | d2 |    |    |  4 |
##  4 |    |    | r1 |    |
matriz = [[2,-1,-1,1],
          [-1,-1,-2,-1],
          [-1,3,-4,-1],
          [2,-1,-1,4],
          [-1,-1,-3,-1]]

estado = 0
texto = input("Introduce el texto a analizar: ")
elementos = lexico.analizador(texto)
e = False
accepted = False
pila.push(0)
a = 0

while(not accepted):
    print(pila)
    input()
    estado = pila.top()##Primer elemento matriz

    #########Segundo elemento matriz##########
    if elementos[a]['token'] == "id":
        recibido = 0
    elif elementos[a]['token'] == "OpSuma":
        recibido = 1
    elif elementos[a]['token'] == "pesos":
        recibido = 2

    if isinstance(estado, EP):
        recibido = 3
        e_cont = pila.pop()
        e = True
        estado = pila.top()
    ##########################################

    accion = matriz[estado][recibido]
    
    if accion == -1:    ####ERROR EN LA CADENA
        print("Cadena no aceptada")
        accepted = True
    elif e:             ####SE RECIBE UN ELEMENTO PILA COMO TOPE POR LO QUE NO HAY DESPLAZAMIENTO
        pila.push(e_cont)
        pila.push(accion)
        e = False
    elif accion >= 0:   ####DESPLAZAMIENTO NORMAL
        pila.push(elementos[a]['lexema'])
        pila.push(accion)
        a+=1
    elif accion == -2:  ####R0
        print("Cadena aceptada")
        pila.pop()
        b = pila.pop()
        print(b)
        accepted = True
    elif accion == -3:  ####R1
        c = EP("E")
        pila.pop()#num
        c.E = pila.pop()#element
        pila.pop()#num
        c.mas = pila.pop()#element
        pila.pop()#num
        c.id = pila.pop()#element
        pila.push(c)
    elif accion == -4:  ####R2
        c = EP("E")
        pila.pop() #num
        c.id = pila.pop() #elemnt
        pila.push(c)
