# https://github.com/minsuk-heo/problemsolving/blob/master/Craking%20the%20Coding%20Interview/2.1_del_dup_linkedlist.py
import unittest
"""
Linked List
Delete Duplicate from linked list
"""

class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)
            
    def print_list(self):
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return str(res)





class UnitTest(unittest.TestCase):
    def test(self):
        ll = LinkedList(3)
        ll.add(4)
        ll.add(5)
        ll.add(6)
        ll.print_list()
        self.assertEqual("[3,4,5,6,7]",ll.print_list())

if __name__ == '__main__':
    unittest.main()