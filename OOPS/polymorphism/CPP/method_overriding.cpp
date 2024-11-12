#include <iostream>
#include <string>
using namespace std;

class Number{
public:

    virtual void print_number(){
        cout << "Number can be an Integer" << endl;
    }
};

class AnotherNumber:public Number{
public:

    void print_number() override {
        cout << "Number can be an Floating Number" << endl;
    }

};


int main(){

    Number num;
    AnotherNumber a_num;
    num.print_number();
    a_num.print_number();

    return 0;
}