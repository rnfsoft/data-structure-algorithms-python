# https://github.com/minsuk-heo/problemsolving/blob/master/Craking%20the%20Coding%20Interview/2.3_remove_node_linkedlist.py

import unittest

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
        cur.next = Node(data)

    def print_list(self):
        cur = self.head
        result = []
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return str(result)
    
    def remove_item(self, item):
        cur = self.head
        if cur.data == item:
            self.head = cur.next
        else:
            prev = None
            while cur is not None:
                if cur.data == item:
                    prev.next = cur.next
                prev = cur
                cur = cur.next
      
class UnitTest(unittest.TestCase):
    def test(self):
        ll = LinkedList(9)
        ll.add(5)
        ll.add(8)
        ll.add(7)
        ll.add(6)
        ll.remove_item(6)
        self.assertEqual('[9, 5, 8, 7]', ll.print_list())

if __name__ == '__main__':
    unittest.main()