#include <iostream>
#include <string>

using namespace std;


int main()
{
    int contador;
    int estado = 0;
    string text;
    string cadena = "";
    cout << "Intoduce el texto a analizar: " << "\n";
    getline(cin,text);
    text = text + " ";
    for(char c : text)
    {
        switch(estado)
        {
            case 0:
            {
                if(int(c)>=48 && int(c)<=57)
                {
                    estado = 1;
                    cadena = cadena+c;
                }
                else if((int(c)>=65 && int(c)<=90)||(int(c)>=97 && int(c)<=122))
                {
                    estado = 2;
                    cadena = cadena+c;
                }
                else if(int(c)==32)
                {
                    cout << cadena << "\t\t\t" << "No valido" << "\n";
                    cadena = "";
                    estado = 0;
                }
                else
                {
                    estado = -1;
                    cadena = cadena+c;
                }
                break;
            }
            case 1:
            {
                if(int(c)>=48 && int(c)<=57)
                {
                    estado = 1;
                    cadena = cadena+c;
                }
                else if(int(c)==46)
                {
                    estado = 3;
                    cadena = cadena+c;
                }
                else if(int(c)==32)
                {
                    cout << cadena << "\t\t\t" << "Entero" << "\n";
                    cadena = "";
                    estado = 0;
                }
                else
                {
                    estado = -1;
                    cadena = cadena+c;
                }
                break;
            }
            case 2:
            {
                if(int(c)>=48 && int(c)<=57)
                {
                    estado = 2;
                    cadena = cadena+c;
                }
                else if((int(c)>=65 && int(c)<=90)||(int(c)>=97 && int(c)<=122))
                {
                    estado = 2;
                    cadena = cadena+c;
                }
                else if(int(c)==95)
                {
                    estado = 2;
                    cadena = cadena+c;
                }
                else if(int(c)==32)
                {
                    cout << cadena << "\t\t\t" << "Identificador" << "\n";
                    cadena = "";
                    estado = 0;
                }
                else
                {
                    estado = -1;
                    cadena = cadena+c;
                }
                break;
            }
            case 3:
            {
                if(int(c)>=48 && int(c)<=57)
                {
                    estado = 4;
                    cadena = cadena+c;
                }
                else if(int(c)==32)
                {
                    cout << cadena << "\t\t\t" << "No valido" << "\n";
                    cadena = "";
                    estado = 0;
                }
                else
                {
                    estado = -1;
                    cadena = cadena+c;
                }
                break;
            }
            case 4:
            {
                if(int(c)>=48 && int(c)<=57)
                {
                    estado = 4;
                    cadena = cadena+c;
                }
                else if(int(c)==32)
                {
                    cout << cadena << "\t\t\t" << "Real" << "\n";
                    cadena = "";
                    estado = 0;
                }
                else
                {
                    estado = -1;
                    cadena = cadena+c;
                }
                break;
            }
            case -1:
            {
                if(int(c)==32)
                {
                    cout << cadena << "\t\t\t" << "No valido" << "\n";
                    cadena = "";
                    estado = 0;
                }
                else
                {
                    cadena = cadena+c;
                }
                break;
            }
        }
    }


    return 0;
}