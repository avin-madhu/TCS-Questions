class CircularQueue():
    def __init__(self,size):
        self.queue = [None]*size
        self.size = size
        self.front = -1
        self.rear = -1
    
    def is_empty(self):
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def add_value(self,value):
        self.rear += (self.rear+1)%self.size
        if self.rear == self.size:
            print("cannot add, queue full")
            self.rear -= 1
            return
        self.queue[self.rear] = value
    
    def remove_value(self):
        if self.is_empty():
            print("empty")
            return
        self.front = None
        self.front += (self.front + 1)%self.size
        
        
    def display_queue(self):
        print(self.queue)

        


    

def main():
    obj = CircularQueue(2)
    obj.add_value(1)
    obj.display_queue()
    obj.add_value(4)
    obj.display_queue()
    obj.add_value(6)
    obj.display_queue()

if __name__ == "__main__":
    main()

