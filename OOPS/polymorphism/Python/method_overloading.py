# This is just a simulation of method overloading as python do not support it (yet)

# given below is a lame one ( maybe cheating )

# we can also simulate method overloading using default parameters in python

class Student:
    def __init__(self):
        pass

    def my_function(*args):
        for name in args:
            print(name)
    
    def my_funcion(*args):
        for name in args:
            print(name)

def main():
    obj = Student()
    obj.my_function("Avin", "Gopika")
    obj.my_function(23,33)

if __name__ == "__main__":
    main()
