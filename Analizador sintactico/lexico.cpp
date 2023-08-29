#include <iostream>

lexico()
{
    lexico::cadena = "";
}


bool is_txt(char c)
{
    if((int(c)>=65 && int(c)<=90)||(int(c)>=97 && int(c)<=122))
        return true;
    else
        return false;
}

bool is_number(char c)
{
    if(int(c)>=48 && int(c)<=57)
        return true;
    else
        return false;
}

bool is_space(char c)
{
    if(int(c)==32)
        return true;
    else
        return false;
}

bool is_sum(char c)
{
    if(int(c)==43||int(c)==45)
        return true;
    else
        return false;
}

bool is_mul(char c)
{
    if(int(c)==42||int(c)==47)
        return true;
    else
        return false;
}

bool is_equal(char c)
{
    if(int(c)==61)
        return true;
    else
        return false;
}

bool is_relat(char c)
{
    if(int(c)==60||int(c)==62)
        return true;
    else
        return false;
}

bool is_and(char c)
{
    if(c == '&')
        return true;
    else
        return false;
}

int id_tipo(string cadena)
{
    for(char c : text)
    {
        switch(estado)
        {
            case 0:
            {
                if(is_number(c))
                {
                    estado = 1;
                    cadena = cadena+c;
                }
                else if(is_txt(c))
                {
                    estado = 2;
                    cadena = cadena+c;
                }
                else if(is_space(c))
                {
                    cout << cadena << "\t\t\t" << "\t No valido" << "\n";
                    cadena = "";
                    estado = 0;
                }
                else if(is_sum(c))
                {
                    estado = 5;
                    tipo_n = 5;
                    tipo_s = "OpSuma";
                    cadena = cadena+c;
                }
                else if(is_mul(c))
                {
                    estado = 5;
                    tipo_n = 6;
                    tipo_s = "OpMul";
                    cadena = cadena+c;
                }
                else if(is_equal(c))
                {
                    estado = 6;
                    cadena = cadena+c;
                }
                else if(is_relat(c))
                {
                    estado = 7;
                    cadena = cadena+c;
                }
                else if(is_and(c))
                {
                    estado = 8;
                    cadena = cadena+c;
                }
                else if(c == '|')
                {
                    estado = 9;
                    cadena = cadena+c;
                }
                else if(c == '!')
                {
                    estado = 10;
                    cadena = cadena+c;
                }
                else if(c == ';')
                {
                    estado = 5;
                    tipo_n = 12;
                    tipo_s = "";
                    cadena = cadena+c;
                }
                else if(c == ',')
                {
                    estado = 5;
                    tipo_n = 13;
                    tipo_s = "";
                    cadena = cadena+c;
                }
                else if(c == '(')
                {
                    estado = 5;
                    tipo_n = 14;
                    tipo_s = "";
                    cadena = cadena+c;
                }
                else if(c == ')')
                {
                    estado = 5;
                    tipo_n = 15;
                    tipo_s = "";
                    cadena = cadena+c;
                }
                else if(c == '{')
                {
                    estado = 5;
                    tipo_n = 16;
                    tipo_s = "";
                    cadena = cadena+c;
                }
                else if(c == '}')
                {
                    estado = 5;
                    tipo_n = 17;
                    tipo_s = "";
                    cadena = cadena+c;
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
                    cout << cadena << "\t\t\t" << "1 \t Entero" << "\n";
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
                    if(cadena == "int"||cadena == "float")
                    {
                        cout << cadena << "\t\t\t" << "4 \t Tipo" << "\n";
                        cadena = "";
                        estado = 0;
                    }
                    else if(cadena == "if")
                    {
                        cout << cadena << "\t\t\t" << "19" << "\n";
                        cadena = "";
                        estado = 0;
                    }
                    else if(cadena == "while")
                    {
                        cout << cadena << "\t\t\t" << "20" << "\n";
                        cadena = "";
                        estado = 0;
                    }
                    else if(cadena == "return")
                    {
                        cout << cadena << "\t\t\t" << "21" << "\n";
                        cadena = "";
                        estado = 0;
                    }
                    else if(cadena == "else")
                    {
                        cout << cadena << "\t\t\t" << "22" << "\n";
                        cadena = "";
                        estado = 0;
                    }
                    else
                    {
                        cout << cadena << "\t\t\t" << "0 \t Identificador" << "\n";
                        cadena = "";
                        estado = 0;
                    }
                    
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
                    cout << cadena << "\t\t\t" << "\t No valido" << "\n";
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
                    cout << cadena << "\t\t\t" << "2 \t Real" << "\n";
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
            case 5:
            {
                if(is_space(c))
                {
                    cout << cadena << "\t\t\t" << tipo_n << "\t" << tipo_s << "\n";
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
            case 6:
            {
                if(is_space(c))
                {
                    cout << cadena << "\t\t\t" << "18" << "\n";
                    cadena = "";
                    estado = 0;
                }
                else if(is_equal(c))
                {
                    cadena = cadena+c;
                    estado = 5;
                    tipo_n = 11;
                    tipo_s = "OpIgualdad";
                }
                else
                {
                    estado = -1;
                    cadena = cadena+c;
                }
                break;
            }
            case 7:
            {
                if(is_space(c))
                {
                    cout << cadena << "\t\t\t" << "7 \t OpRelac" << "\n";
                    cadena = "";
                    estado = 0;
                }
                else if(is_equal(c))
                {
                    cadena = cadena+c;
                    estado = 5;
                    tipo_n = 7;
                    tipo_s = "OpRelac";
                }
                else
                {
                    estado = -1;
                    cadena = cadena+c;
                }
                break;
            }
            case 8:
            {
                if(is_and(c))
                {
                    cadena = cadena+c;
                    estado = 5;
                    tipo_n = 9;
                    tipo_s = "OpAnd";
                }
                else
                {
                    estado = -1;
                    cadena = cadena+c;
                }
                break;
            }
            case 9:
            {
                if(c == '|')
                {
                    cadena = cadena+c;
                    estado = 5;
                    tipo_n = 8;
                    tipo_s = "OpOr";
                }
                else
                {
                    estado = -1;
                    cadena = cadena+c;
                }
                break;
            }
            case 10:
            {
                if(is_space(c))
                {
                    cout << cadena << "\t\t\t" << "10 \t OpNot" << "\n";
                    cadena = "";
                    estado = 0;
                }
                else if(c == '=')
                {
                    cadena = cadena+c;
                    estado = 5;
                    tipo_n = 11;
                    tipo_s = "OpIgualdad";
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
                    cout << cadena << "\t\t\t" << "\t No valido" << "\n";
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
}

