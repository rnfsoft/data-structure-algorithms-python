# https://github.com/minsuk-heo/problemsolving/blob/master/Craking%20the%20Coding%20Interview/2.1_del_dup_linkedlist.py
import unittest
"""
Linked List
Delete Duplicate from linked list
"""

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
        

    def delete_duplicate(self):
        cur = self.head
        prev = None
        dict = {}
        while cur is not None:
            if cur.data in dict:
                prev.next = cur.next
            else:
                dict[cur.data] = True
                prev = cur
            cur = cur.next

class UnitTest(unittest.TestCase):
    def test(self):
        ll = LinkedList(3)
        ll.add(4)
        ll.add(5)
        ll.add(6)
        ll.add(4)
        ll.add(7)
        ll.add(4)
        ll.add(6)
        ll.add(6)
        ll.delete_duplicate()
        self.assertEqual("[3, 4, 5, 6, 7]", ll.print_list())

if __name__ == '__main__':
    unittest.main()