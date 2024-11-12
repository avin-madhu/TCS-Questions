#include <iostream>
#include <map>
#include <string>
using namespace std;

void display_map(map<char,int> m){
    for(auto pair: m){
        cout << pair.first << " : " << pair.second << endl;
    }
}

int main()
{
    map<char, int> count;
    string str = "aavinavi";
    for(char ch: str){
        if(!count.count(ch)){
            count.insert({ch,1});
        }
        else
        {
            count.at(ch) += 1;
        }
    }
    display_map(count);
    return 0;
}