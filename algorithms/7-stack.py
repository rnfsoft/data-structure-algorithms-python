import unittest

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        if len(self.items) < 5:
            self.items.append(item)
        else:
            print('Stack Over Flow') # DO NOT FORGET THIS

    def pop(self):
        if len(self.items) > 0: # DO NOT FORGET THIS
            self.items.pop()
        else:
            print('Stack Under Flow')  # DO NOT FORGET THIS

    def peek(self):
        self.items[-1]
    
    def print_items(self):
        print(self.items)

class UnitTest(unittest.TestCase):
    def test(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.print_items()
        s.pop()
        s.pop()
        s.pop()
        s.print_items()
        

if __name__ == '__main__':
    unittest.main()

