
#include <bits/stdc++.h>
 
using namespace std;
 
int main()
{
    string texto;
    vector<string> v;
    string s;
    
    getline(cin,texto);
    stringstream ss(texto);
    
    while (getline(ss, s, ' ')) {
        v.push_back(s);
    }
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << endl;
    }
 
    return 0;
}