class Student():
    def __init__(self,name):
        self.name = name
    
    def get_name(self):
        print(self.name)
    
    def set_name(self,new_name):
        self.name = new_name

def main():
    obj = Student("Avin")
    obj.get_name()
    obj.set_name("Gopika")
    obj.get_name()
    
if __name__ == "__main__":
    main()