#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-binary-search-tree-exercise-3.php

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_BST(root):
    stack = []
    prev = None
    
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and root.data <= prev.data:
            return False
        prev = root
        root = root.right
    return True

root = Node(3) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(4) 
  
if is_BST(root): 
    print("is BST") 
else: 
    print("not a BST") 