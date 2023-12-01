variables = []
funciones = []
num_if = 0
num_if_cump = 0
num_if_nocump = 0

def get_termino(termino):
    global variables
    try:
        valor = termino.entero
        valor = int(valor)
    except AttributeError:
        try:
            valor = termino.real
            valor = float(valor)
        except AttributeError:
            try:
                valor = termino.cadena
            except AttributeError:
                for b in variables:
                    if(b["id"]==termino.identificador):
                        #valor = b["valor"]
                        valor = termino.identificador + "_" + b["contexto"]
    return valor

def sum(expresion):
    a=0
    b=0
    termino = expresion.Expresion.Termino
    a = get_termino(termino)
    
    try:
        termino = expresion.Expresion2.Termino
        sub_op = None
        print("MOV AX,",get_termino(termino))
    except AttributeError:
        try:
            sub_op = expresion.Expresion2.opSum
        except AttributeError:
            try:
                sub_op = expresion.Expresion2.opMul
            except AttributeError:
                sub_op = None
    if(sub_op == "+"):
        #b = sum(expresion.Expresion2)
        sum(expresion.Expresion2)
    elif(sub_op == "-"):
        #b = res(expresion.Expresion2)
        res(expresion.Expresion2)
    elif(sub_op == "*"):
        #b = mul(expresion.Expresion2)
        mul(expresion.Expresion2)
    elif(sub_op == "/"):
        #b = div(expresion.Expresion2)
        div(expresion.Expresion2)
    print("MOV BX,",a)
    print("ADD AX,BX")
    #return(a+b)

def res(expresion):
    a=0
    b=0
    termino = expresion.Expresion.Termino
    a = get_termino(termino)
    
    try:
        termino = expresion.Expresion2.Termino
        sub_op = None
        print("MOV AX,",get_termino(termino))
    except AttributeError:
        try:
            sub_op = expresion.Expresion2.opSum
        except AttributeError:
            try:
                sub_op = expresion.Expresion2.opMul
            except AttributeError:
                sub_op = None
    if(sub_op == "+"):
        #b = sum(expresion.Expresion2)
        sum(expresion.Expresion2)
    elif(sub_op == "-"):
        #b = res(expresion.Expresion2)
        res(expresion.Expresion2)
    elif(sub_op == "*"):
        #b = mul(expresion.Expresion2)
        mul(expresion.Expresion2)
    elif(sub_op == "/"):
        #b = div(expresion.Expresion2)
        div(expresion.Expresion2)
    print("MOV BX,",a)
    print("SUB AX,BX")
    #return(a-b)

def mul(expresion):
    a=0
    b=0
    termino = expresion.Expresion.Termino
    a = get_termino(termino)
    
    try:
        termino = expresion.Expresion2.Termino
        sub_op = None
        print("MOV AX,",get_termino(termino))
    except AttributeError:
        try:
            sub_op = expresion.Expresion2.opSum
        except AttributeError:
            try:
                sub_op = expresion.Expresion2.opMul
            except AttributeError:
                sub_op = None
    if(sub_op == "+"):
        #b = sum(expresion.Expresion2)
        sum(expresion.Expresion2)
    elif(sub_op == "-"):
        #b = res(expresion.Expresion2)
        res(expresion.Expresion2)
    elif(sub_op == "*"):
        #b = mul(expresion.Expresion2)
        mul(expresion.Expresion2)
    elif(sub_op == "/"):
        #b = div(expresion.Expresion2)
        div(expresion.Expresion2)
    print("MOV BX,",a)
    print("MUL BX")
    #return(a*b)

def div(expresion):
    a=0
    b=0
    termino = expresion.Expresion.Termino
    a = get_termino(termino)
    
    try:
        termino = expresion.Expresion2.Termino
        sub_op = None
        print("MOV AX,",get_termino(termino))
    except AttributeError:
        try:
            sub_op = expresion.Expresion2.opSum
        except AttributeError:
            try:
                sub_op = expresion.Expresion2.opMul
            except AttributeError:
                sub_op = None
    if(sub_op == "+"):
        #b = sum(expresion.Expresion2)
        sum(expresion.Expresion2)
    elif(sub_op == "-"):
        #b = res(expresion.Expresion2)
        res(expresion.Expresion2)
    elif(sub_op == "*"):
        #b = mul(expresion.Expresion2)
        mul(expresion.Expresion2)
    elif(sub_op == "/"):
        #b = div(expresion.Expresion2)
        div(expresion.Expresion2)
    print("MOV BX,",a)
    print("DIV BX")
    #return(a*b)

def describir_if(condicion):
    global num_if
    num_if+=1
    try:
        operando = condicion.opIgualdad
    except AttributeError:
        try:
            operando = condicion.opRelac
        except AttributeError:
            operando = None

    a = get_termino(condicion.Expresion.Termino)
    b = get_termino(condicion.Expresion2.Termino)
    print("MOV AX,",a)
    print("MOV BX,",b)
    print("CMP AX,BX")
    
    if(operando == "=="):
        print("JE ETIQ_CUMP",num_if,sep="")
        print("JMP ETIQ_NOCUMP",num_if,sep="")
    elif(operando == ">"):
        print("JA ETIQ_CUMP",num_if,sep="")
        print("JMP ETIQ_NOCUMP",num_if,sep="")
    elif(operando == ">="):
        print("JAE ETIQ_CUMP",num_if,sep="")
        print("JMP ETIQ_NOCUMP",num_if,sep="")
    elif(operando == "<"):
        print("JB ETIQ_CUMP",num_if,sep="")
        print("JMP ETIQ_NOCUMP",num_if,sep="")
    elif(operando == "<="):
        print("JBE ETIQ_CUMP",num_if,sep="")
        print("JMP ETIQ_NOCUMP",num_if,sep="")

def condicion_or(sentencia):
    global num_if_nocump
    global num_if_cump
    condicion1 = sentencia.Expresion
    describir_if(condicion1)
    num_if_nocump+=1
    print("ETIQ_NOCUMP",num_if_nocump,":",sep="")

    condicion2 = sentencia.Expresion2
    try:
        operando = condicion2.opOr
    except AttributeError:
        try:
            operando = condicion2.opAnd
        except AttributeError:
            operando = None
    
    if(operando == "&&"):
        condicion_and(condicion2)
    elif(operando == "||"):
        condicion_or(condicion2)
    else:
        describir_if(condicion2)
        while(num_if_cump<=num_if_nocump):
            num_if_cump+=1
            print("ETIQ_CUMP",num_if_cump,":",sep="")
        print("Sentencia bloque")
        num_if_nocump+=1
        print("ETIQ_NOCUMP",num_if_nocump,":",sep="")





def condicion_and(sentencia):
    global num_if_nocump
    global num_if_cump
    condicion1 = sentencia.Expresion
    describir_if(condicion1)
    num_if_cump+=1
    print("ETIQ_CUMP",num_if_cump,":",sep="")

    condicion2 = sentencia.Expresion2
    try:
        operando = condicion2.opOr
    except AttributeError:
        try:
            operando = condicion2.opAnd
        except AttributeError:
            operando = None
    
    if(operando == "&&"):
        condicion_and(condicion2)
    elif(operando == "||"):
        condicion_or(condicion2)
    else:
        describir_if(condicion2)
        num_if_cump+=1
        print("ETIQ_CUMP",num_if_cump,":",sep="")
        print("Sentencia bloque")
        num_if_nocump+=1
        while(num_if_nocump<=num_if_cump):
            print("ETIQ_NOCUMP",num_if_nocump,":",sep="")
            num_if_nocump+=1


def analizador(arbol):
    #print(arbol)
    global variables
    global funciones
    global num_if_cump
    global num_if_nocump
    arbol_2 = arbol
    print(";-----------------------------------")
    print(".DATA")
    if (arbol):
        arbol = arbol.Definiciones
        while(arbol):                   ##PARA DESPLAZARSE EN DEFINICIONES
            definicion = arbol.Definicion
            #######################################VARIABLES GLOBALES############################################
            defvar = None
            try:
                defvar = definicion.DefVar
            except AttributeError:
                pass
            if(defvar):
                tipo = defvar.tipo
                while(defvar):
                    variables.append({'id':defvar.identificador,'tipo':tipo,'valor':None,'contexto':"global"})
                    print(defvar.identificador,"_global DW ?",sep="")
                    try:
                        defvar = defvar.ListaVar.extra
                    except AttributeError:
                        defvar = defvar.ListaVar
            ####################################################################################################

            ###################################FUNCIONES Y SUS VARIABLES########################################
            deffun = None
            try:
                deffun = definicion.DefFunc
            except AttributeError:
                pass
            if(deffun):
                funcion = deffun.identificador
                funciones.append({'id':deffun.identificador,'tipo':deffun.tipo})
                try:
                    param = deffun.Parametros.extra     ##Se verifica que si haya parametros
                except AttributeError:
                    param = deffun.Parametros
                while(param):
                    variables.append({'id':param.identificador,'tipo':param.tipo,'valor':None,'contexto':funcion})
                    print(param.identificador,"_" , funcion , " DW ?",sep="")
                    try:
                        param = param.ListaParam.extra
                    except AttributeError:
                        param = param.ListaParam
                bloc = deffun.BloqFunc
                try:
                    bloc = bloc.DefLocales.extra        ##Se verifica que exista algo dentro de la funcion
                except AttributeError:
                    bloc = bloc.DefLocales
                while(bloc):
                    try:
                        defvar = bloc.DefLocal.DefVar     ##Se verifica que se definan variables
                    except AttributeError:
                        defvar = None
                    if(defvar):
                        tipo = defvar.tipo
                        while(defvar):
                            variables.append({'id':defvar.identificador,'tipo':tipo,'valor':None,'contexto':funcion})
                            print(defvar.identificador,"_" , funcion , " DW ?",sep="")
                            try:
                                defvar = defvar.ListaVar.extra
                            except AttributeError:
                                defvar = defvar.ListaVar

                    try:
                        bloc = bloc.DefLocales.extra
                    except AttributeError:
                        bloc = bloc.DefLocales
            ###################################################################################################

            try:
                arbol = arbol.Definiciones.extra
            except AttributeError:
                arbol = arbol.Definiciones

    print(";-----------------------------------")
    print(".CODE")
    print("BEGIN PROC FAR")
    print("MOV AX,@DATA")
    print("MOV DS,AX")

    if(arbol_2):
        arbol_2 = arbol_2.Definiciones
        while(arbol_2):                   ##PARA DESPLAZARSE EN DEFINICIONES
            definicion = arbol_2.Definicion
            ###################################ASIGNACIONES DE VARIABLES########################################
            deffun = None
            try:
                deffun = definicion.DefFunc
            except AttributeError:
                pass
            if(deffun):
                funcion = deffun.identificador
                bloc = deffun.BloqFunc
                try:
                    bloc = bloc.DefLocales.extra        ##Se verifica que exista algo dentro de la funcion
                except AttributeError:
                    bloc = bloc.DefLocales
                while(bloc):
                    try:
                        sentencia = bloc.DefLocal.Sentencia.identificador     ##Se verifica que se tenga una sentencia de asignacion
                        sentencia = bloc.DefLocal.Sentencia
                    except AttributeError:
                        sentencia = None
                    if(sentencia):
                        id = sentencia.identificador
                        ##########################ASIGNACIONES DIRECTAS#############################
                        try:
                            expresion = sentencia.Expresion.Termino
                        except AttributeError:
                            expresion = None
                        if(expresion):
                            for a in variables:
                                if(a["id"]==id):
                                    a["valor"] = get_termino(expresion)
                                    print("MOV CX,",get_termino(expresion))
                                    print("MOV ",id,"_",a["contexto"]," , CX",sep="")
                        ###########################################################################

                        #########################OPERACIONES ARITMETICAS###########################
                        try:
                            operacion = sentencia.Expresion.opSuma
                            expresion = sentencia.Expresion
                        except AttributeError:
                            try:
                                operacion = sentencia.Expresion.opMul
                                expresion = sentencia.Expresion
                            except AttributeError:
                                operacion = None
                                expresion = None
                        if(operacion == "+"):
                            for i in variables:
                                if(i["id"] == id):
                                    #i["valor"]=sum(expresion)
                                    sum(expresion)
                                    print("MOV ",id,"_",i["contexto"]," , AX",sep="")
                        elif(operacion == "-"):
                            for i in variables:
                                if(i["id"] == id):
                                    #i["valor"]=res(expresion)
                                    res(expresion)
                                    print("MOV ",id,"_",i["contexto"]," , AX",sep="")
                        elif(operacion == "*"):
                            for i in variables:
                                if(i["id"] == id):
                                    #i["valor"]=mul(expresion)
                                    mul(expresion)
                                    print("MOV ",id,"_",i["contexto"]," , AX",sep="")
                        elif(operacion == "/"):
                            for i in variables:
                                if(i["id"] == id):
                                    #i["valor"]=div(expresion)
                                    div(expresion)
                                    print("MOV ",id,"_",i["contexto"]," , AX",sep="")
                        ###########################################################################

                    try:
                        sentencia = bloc.DefLocal.Sentencia.palabraif     ##Se verifica que se tenga una sentencia de if
                        sentencia = bloc.DefLocal.Sentencia
                    except AttributeError:
                        sentencia = None
                    if(sentencia):
                        condicion = sentencia.Expresion
                        try:
                            operando = condicion.opOr
                        except AttributeError:
                            try:
                                operando = condicion.opAnd
                            except AttributeError:
                                operando = None
                        
                        if(operando == "&&"):
                            condicion_and(condicion)
                        elif(operando == "||"):
                            condicion_or(condicion)
                        else:
                            describir_if(condicion)
                            num_if_cump+=1
                            print("ETIQ_CUMP",num_if_cump,":",sep="")
                            print("Sentencia bloque")
                            num_if_nocump+=1
                            print("ETIQ_NOCUMP",num_if_nocump,":",sep="")

                    try:
                        bloc = bloc.DefLocales.extra
                    except AttributeError:
                        bloc = bloc.DefLocales
            ###################################################################################################

            try:
                arbol_2 = arbol_2.Definiciones.extra
            except AttributeError:
                arbol_2 = arbol_2.Definiciones

    print("\n")
    print("FUNCIONES")
    print("ID","\t","TIPO")
    for a in funciones:
        print(a["id"],"\t",a["tipo"])

    print("\n")
    print("VARIABLES")
    print("ID","\t","TIPO","\t","VALOR","\t","CONTEXTO")
    for a in variables:
        print(a["id"],"\t",a["tipo"],"\t",a["valor"],"\t",a["contexto"])


#Sigue sentencia bloque del if... D: