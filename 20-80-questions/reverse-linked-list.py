class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)

    def print_list(self):
        cur = self.head
        while cur:
            print (cur.data)
            cur = cur.next
    
    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev


ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.print_list()

ll.reverse()
ll.print_list()


