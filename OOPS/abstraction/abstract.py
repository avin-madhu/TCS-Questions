from abc import ABC, abstractmethod

class Student(ABC):

    @abstractmethod
    def print_details(self):
        ...

class Derived_class(Student):
    def print_details(self):
        print("student details printed")

obj = Derived_class()
obj.print_details()

# A thing to learn here is when we call print_details python automatically
# passes the object we made to the method (obj in this case) hence it is 
# important that we put 'self' in the parameter to recieve this else error occurs


# Abstract methods do not have implementation
# They are used to hide complex data from the code