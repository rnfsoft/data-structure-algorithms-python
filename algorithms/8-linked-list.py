import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)
    
    def remove(self, item):
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
    
    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev # DO NOT FORGET THIS
    

