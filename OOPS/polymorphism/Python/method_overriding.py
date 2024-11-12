class StudentA():
    def __init__(self):
        self.name = "Avin"
    
    def print_name(self):
        print("hi I am ",self.name)

class StudentB(StudentA):
    def __init__(self):
        self.name = "Gopika"
    
    def print_name(self):
        print("hi I am ",self.name)

def main():
    A = StudentA()
    B = StudentB()

    A.print_name()
    B.print_name()

if __name__ == "__main__":
    main()


"""
This is an example of run time polymorphism

but method overloading is compile time polymorphism but python does not support it
but there are ways to simulate it ( explore )

"""


