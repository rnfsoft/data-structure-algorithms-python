class Stack:
    

    def __init__(self):
        self.items = []
        self.stack_size = 5

    def push(self, data):
        if len(self.items) < self.stack_size:
            self.items.append(data)           
        else:
            print ("Stack Over Flow")
            

    def pop(self):
        if len(self.items) > 0:
            self.items.pop()
        else:
            print ("Stack Under Flow")

    def peek(self):
        return self.items[-1]

    def print_list(self):
        print(self.items)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.print_list()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
