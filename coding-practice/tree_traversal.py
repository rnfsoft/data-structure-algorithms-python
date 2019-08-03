# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)


n = Node(1)
n.left = Node(2)
n.right = Node(3)
n.left.left = Node(4)
n.left.right = Node(5)
print('Inorder')
inorder(n)
print('preorder')
preorder(n)
print('postorder')
postorder(n)
