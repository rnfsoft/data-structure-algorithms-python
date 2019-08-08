class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


def is_circular(head):
    if head==None: 
        return True
    node = head.next
    while((node is not None) and (node is not head)): 
        node = node.next
    return(node==head) 

def isCircular(head):

    slow = head
    fast = head

    while fast != None:
        slow = slow.next

        if fast.next != None:
             fast = fast.next.next
        else:
             return False

        if slow is fast:
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

if isCircular(ll.head):
    print ('Yes')
else:
    print ('No')
    

fourth.next = ll.head 
      
if is_circular(ll.head): 
    print('Yes') 
else: 
    print('No')
    
if isCircular(ll.head):
    print ('Yes')
else:
    print ('No')
