variables = []
funciones = []

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
                        valor = b["valor"]
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
        b = sum(expresion.Expresion2)
    elif(sub_op == "-"):
        b = res(expresion.Expresion2)
    elif(sub_op == "*"):
        b = mul(expresion.Expresion2)
    elif(sub_op == "/"):
        b = div(expresion.Expresion2)
    elif(termino):
        b = get_termino(termino)
    print("MOV BX,",a)
    print("ADD AX,BX")
    return(a+b)

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
        b = sum(expresion.Expresion2)
    elif(sub_op == "-"):
        b = res(expresion.Expresion2)
    elif(sub_op == "*"):
        b = mul(expresion.Expresion2)
    elif(sub_op == "/"):
        b = div(expresion.Expresion2)
    elif(termino):
        b = get_termino(termino)
    print("MOV BX,",a)
    print("SUB AX,BX")
    return(a-b)

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
        b = sum(expresion.Expresion2)
    elif(sub_op == "-"):
        b = res(expresion.Expresion2)
    elif(sub_op == "*"):
        b = mul(expresion.Expresion2)
    elif(sub_op == "/"):
        b = div(expresion.Expresion2)
    elif(termino):
        b = get_termino(termino)
    print("MOV BX,",a)
    print("MUL BX")
    return(a*b)

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
        b = sum(expresion.Expresion2)
    elif(sub_op == "-"):
        b = res(expresion.Expresion2)
    elif(sub_op == "*"):
        b = mul(expresion.Expresion2)
    elif(sub_op == "/"):
        b = div(expresion.Expresion2)
    elif(termino):
        b = get_termino(termino)
    print("MOV BX,",a)
    print("DIV BX")
    return(a*b)

def analizador(arbol):
    #print(arbol)
    global variables
    global funciones
    arbol_2 = arbol
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
                    variables.append({'id':defvar.identificador,'tipo':tipo,'valor':None,'contexto':"#"})
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
                                    i["valor"]=sum(expresion)
                        elif(operacion == "-"):
                            for i in variables:
                                if(i["id"] == id):
                                    i["valor"]=res(expresion)
                        elif(operacion == "*"):
                            for i in variables:
                                if(i["id"] == id):
                                    i["valor"]=mul(expresion)
                        elif(operacion == "/"):
                            for i in variables:
                                if(i["id"] == id):
                                    i["valor"]=div(expresion)
                        ###########################################################################

                    try:
                        sentencia = bloc.DefLocal.Sentencia.palabraif     ##Se verifica que se tenga una sentencia de asignacion
                        sentencia = bloc.DefLocal.Sentencia
                    except AttributeError:
                        sentencia = None
                    if(sentencia):
                        condicion = sentencia.Expresion
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
                            print("JE etiqueta")
                        elif(operando == ">"):
                            print("JA etiqueta")
                        elif(operando == ">="):
                            print("JAE etiqueta")
                        elif(operando == "<"):
                            print("JB etiqueta")
                        elif(operando == "<="):
                            print("JBE etiqueta")

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


# NOTAS PORQUE ESTOY VIENDO COMO HACER EL if
# CMP PARA COMPARAR QUE ESTÁ PASANDO
# CMP AX,BX
# JE ES PARA COMPARAR SI SON IGUALES
# JA SI ES MAYOR (AX>BX)
# JAE SI ES MAYOR O IGUAL (AX>=BX)
# JB SI ES MENOR (AX<BX)
# JBE SI ES MENOR O IGUAL (AX<=BX)