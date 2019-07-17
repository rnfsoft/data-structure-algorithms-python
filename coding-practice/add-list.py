# https://github.com/minsuk-heo/problemsolving/blob/master/Craking%20the%20Coding%20Interview/2.5_add_lists.py
"""
Linked List
input: 7-1-6, 5-9-2 # 617 + 295
output: 912
add two linked list and return int value
"""

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

    def reverse(self):
        cur = self.head
        prev = None
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def get_head(self):
        return self.head

def convert_number(ll):
    ll.reverse()
    cur = ll.get_head()
    result = []
    while cur is not None:
        result.append(str(cur.data))
        cur = cur.next
    return int(''.join(result))

def add_list(ll1, ll2):
    return convert_number(ll1) + convert_number(ll2)
    

class UnitTest(unittest.TestCase):
    def test(self):
        ll1 = LinkedList(7)
        ll1.add(1)
        ll1.add(6)

        ll2 = LinkedList(5)
        ll2.add(9)
        ll2.add(2)
        self.assertEqual(912, add_list(ll1, ll2))


if __name__ == '__main__':
    unittest.main()
        