#include <iostream>
#include <string>
using namespace std;

class Number{
public:

    void print_number(int num){
        cout << num << endl;
    }

    void print_number(double num){
        cout << num << endl;
    }

};

int main(){

    Number num;
    num.print_number(20);
    num.print_number(20.3453);
    
    return 0;
}