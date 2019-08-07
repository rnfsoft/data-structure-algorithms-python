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


def isBST(root, l = None, r = None):
    if root == None:
        return True
    
    if (l != None and root.data <= l.data):
        return False

    if (r != None and root.data >= r.data):
        return False

    return isBST(root.left, l, root) and isBST(root.right, root, r)


root = Node(3) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(4) 
  
if is_BST(root): 
    print("is BST") 
else: 
    print("not a BST") 

if isBST(root): 
    print("is BST") 
else: 
    print("not a BST") 


root2 = Node(4) 
root2.left = Node(2) 
root2.right = Node(5) 
root2.left.left = Node(1) 
root2.left.right = Node(3)

if is_BST(root2): 
    print("is BST") 
else: 
    print("not a BST") 

if isBST(root2): 
    print("is BST") 
else: 
    print("not a BST") 