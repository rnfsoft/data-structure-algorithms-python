class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


def is_circular(input):
    cur = input.head
    while cur.next:
        cur = cur.next
        if cur.next == input.head:
            return True
    return False

ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

ll.head.next = second
second.next = third
third.next = fourth
if is_circular(ll.head):
    print ('Yes')
else:
    print ('No')
