#include <iostream>
#include <string>
using namespace std;

class Student{
private:
    string name = "Avin";

public:
    void get_name(){
        cout<< name << endl;
    }

    void set_name(string new_name){
        name = new_name;
    }

};

int main(){

    Student obj;
    obj.get_name();
    obj.set_name("Gopika");
    obj.get_name();
    return 0;
}

/*
 
 so basially why we do this is because we can restrict user to set the data as they want 
 let's say if we want to put a condition like set age only if age > 18, in such situations
 encapsulation concept helps.

*/
