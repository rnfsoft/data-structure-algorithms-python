# https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
# Lowest Common Ancestor in BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lca(root, n1, n2):
    while root:
        if root.data > n1 and root.data > n2:
            root = root.left
        elif root.data < n1 and root.data < n2:
            root = root.right
        else:
            break
    return root

# Use this method
def LCA(root, n1, n2):
    if root is None:
        return None

    if (root.data > n1 and root.data > n2):
        return LCA(root.left, n1, n2)

    if (root.data < n1 and root.data < n2):
        return LCA(root.right, n1, n2)

    return root

root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14)
t1 = lca(root, 10, 14)
print (t1.data)
T1 = LCA(root, 10, 14)
print (T1.data)

t2 = lca(root, 14, 8)
print (t2.data)
T2 = LCA(root, 14, 8)
print (T2.data)



