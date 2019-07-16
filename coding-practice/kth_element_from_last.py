# https://github.com/minsuk-heo/problemsolving/blob/master/Craking%20the%20Coding%20Interview/2.2_k_th_from_last_linkedlist.py

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
    
    def kth_element_from_last(self, n):
        p1 = self.head
        count = 0
        while p1 is not None:
            p1 = p1.next
            count += 1

        # count = 7

        if n > count -1:
            return None

        p2 = self.head
        for i in range(count-1-n):
            p2 = p2.next
        return p2.data

class UnitTest(unittest.TestCase):
    def test(self):
        ll = LinkedList(3)
        ll.add(4)
        ll.add(5)
        ll.add(6)
        ll.add(4)
        ll.add(7)
        ll.add(4)
        ll.print_list()
        self.assertEqual(4, ll.kth_element_from_last(0))
        self.assertEqual(7, ll.kth_element_from_last(1))
        self.assertEqual(4, ll.kth_element_from_last(2))
        self.assertEqual(6, ll.kth_element_from_last(3))
        self.assertEqual(5, ll.kth_element_from_last(4))
        self.assertEqual(4, ll.kth_element_from_last(5))
        self.assertEqual(3, ll.kth_element_from_last(6))
        self.assertEqual(None, ll.kth_element_from_last(7))


if __name__ == '__main__':
    unittest.main()