import lexico
import sintactico
import semantico

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
semantico.analizador(arbol)

