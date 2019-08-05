# https://github.com/minsuk-heo/coding_interview_kr/blob/master/%EC%9D%B4%EC%A7%84%ED%8A%B8%EB%A6%AC_%EC%A2%8C%EC%9A%B0%EB%B0%98%EC%A0%84%EC%8B%9C%ED%82%A4%EA%B8%B0.ipynb
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def invert_tree(node):
    if not node:
        return None
    node.left, node.right = node.right, node.left
    invert_tree(node.left)
    invert_tree(node.right)
    return node

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

t = Node(1)
t.left = Node(2)
t.right = Node(3)
t.left.left = Node(4)
t.left.right = Node(5)
t.right.left = Node(6)
t.right.right = Node(7)

preorder(t)
invert_tree(t)
preorder(t)