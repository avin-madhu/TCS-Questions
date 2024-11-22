#include <iostream>
using namespace std;
#include <string>

class Student{
public:
    virtual void print_details(); // abstract method
};

class Student_derived:Student{
public:
    void print_details() override {
        cout<<"Hello";
    }
};

int main(){
    Student_derived obj;
    obj.print_details();
}