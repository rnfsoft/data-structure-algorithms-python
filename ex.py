class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next= Node(data)
    
    def reverse(self):
        cur = self.head
        prev = None
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def print_list(self):
        cur = self.head
        l = []
        while cur is not None:
            l.append(cur.data)
            cur = cur.next
        return l

ll = LinkedList(1)
ll.add(2)
ll.add(3)
ll.add(2)
ll.add(2)

input = ll.print_list()
ll.reverse()
output = ll.print_list()

print(True if input == output else False)
