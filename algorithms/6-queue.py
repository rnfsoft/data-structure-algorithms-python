import unittest

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def print_queue(self):
        print(self.items)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class UnitTest(unittest.TestCase):
    def test(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.print_queue()

if __name__ == '__main__':
    unittest.main()