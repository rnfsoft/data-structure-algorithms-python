"""
stack has min function O(1)
"""
import unittest

# class stack():
#     def __init__(self):
#         self.items = []
#         self.mins = []
#         self.min = None

#     def push(self, item):
#         self.items.append(item)
#         if self.min is not None:
#             self.mins.append(self.min)
#         if self.min is None or self.min > item:
#             self.min = item

#     def pop(self):
#         self.items.pop()
#         self.min = self.mins.pop()

#     def getminimum(self):
#         return self.min

#     def peak(self):
#         return self.items[-1]

import unittest
class Stack:
    def __init__(self):
        self.items = []
        self.mins = []
        self.min = None
    
    def push(self, data):
        self.items.append(data)
        if self.min is None or self.min > data:
            self.min = data
            self.mins.append(self.min)
    
    def pop(self):
        a = self.items.pop()
        if a == self.min:
            self.mins.pop()
            self.min = self.mins[-1]

    def getminimum(self):
        return self.min

    def peak(self):
        return self.items[-1]



    

class test(unittest.TestCase):
    def test(self):
        st = Stack()
        st.push(5)
        self.assertEqual(5, st.getminimum())
        st.push(3)
        self.assertEqual(3, st.getminimum())
        self.assertEqual(3, st.peak())
        st.pop()
        self.assertEqual(5, st.getminimum())

if __name__ == '__main__':
    unittest.main()