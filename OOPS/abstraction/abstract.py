from abc import ABC, abstractmethod

class college():

    @abstractmethod
    def enroll(self):
        pass

class student(college):

    def enroll(self):
        print("Enrolled")

def main():

    obj = student()
    obj.enroll()

if __name__ == "__main__":
    main()




