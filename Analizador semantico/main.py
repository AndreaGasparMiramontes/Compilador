import lexico
import sintactico

#texto = input("Introduce el texto a analizar: ")
texto = ""
archivo = open("codigo.me",mode="r",encoding="utf-8")
while(True):
    linea = archivo.readline()
    if not linea:
        break
    texto = texto + linea
archivo.close()
print(texto)
elementos = lexico.analizador(texto)
arbol = sintactico.analizador(elementos)
#print(arbol)
variables = []
funciones = []
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

