#include <string>
#include <lexico.cpp>

using namespace std;

class lexico
{
private:
    string cadena;

    bool is_txt(char c)
    bool is_number(char c)
    bool is_space(char c)
    bool is_sum(char c)
    bool is_mul(char c)
    bool is_equal(char c)
    bool is_relat(char c)
    bool is_and(char c)

public:
    lexico();
    int id_tipo(string cadena);
}