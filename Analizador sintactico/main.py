import lexico

##    | id |  + |  $ |  E |
##  0 | d2 |    |    |  1 |
##  1 |    |    | r0 |    |
##  2 |    | d3 | r2 |    |
##  3 | d2 |    |    |    |
##  4 |    |    | r1 |    |
arreglo = [[2,0,0,1],[0,0,-1,0],[0,3,-3,0],[0,2,0,0],[0,0,-2,0]]

estado = 0

texto = input("Introduce el texto a analizar: ")
elementos = lexico.analizador(texto)
for elemento in elementos:
    print("Lexema: ",elemento['lexema'],"Token: ",elemento['token'],"num: ",elemento['num'])
    if estado == 0:
        if elemento['token'] == "id":
            #agregar a pila el elemento y el numero 2
            pass
        elif elemento['token'] == "E":
            #agregar a pila el elemento y el numero 2
            pass
