# https://github.com/minsuk-heo/problemsolving/blob/master/Craking%20the%20Coding%20Interview/2.7_palindrome_linkedlist.py
"""
Palindrome
a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
1-3-5-3-1 is palindrome
5-9-2 is not palindrome
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

    def print_list(self):
        cur = self.head
        result = []
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return str(result)

def pailndrome(ll):
    input = ll.print_list()
    ll.reverse() # after reverse then assing variable 
    output = ll.print_list()
    return True if input == output else False


class UnitTest(unittest.TestCase):
    def test(self):
        ll = LinkedList(1)
        ll.add(3)
        ll.add(5)
        ll.add(3)
        ll.add(1)
        self.assertTrue(pailndrome(ll))


if __name__ == '__main__':
    unittest.main()


