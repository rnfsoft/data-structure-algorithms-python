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


def is_bst_satisfied(root):
    if root:
        is_satisfied = _is_bst_satisfiled(root, root.data)
        if is_satisfied is None:
            return True
        return False
    return True



def _is_bst_satisfiled(cur_node, data):
    if cur_node.left:
        if data > cur_node.left.data:
            return _is_bst_satisfiled(cur_node.left, cur_node.left.data)
        else:
            return False
    if cur_node.right:
        if data < cur_node.right.data:
            return _is_bst_satisfiled(cur_node.right, cur_node.right.data)
        else:
            return False

root = Node(3) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(4) 
  
if is_BST(root): 
    print("is BST") 
else: 
    print("not a BST") 

if is_bst_satisfied(root): 
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

if is_bst_satisfied(root2): 
    print("is BST") 
else: 
    print("not a BST") 
