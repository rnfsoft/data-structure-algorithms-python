# https://www.geeksforgeeks.org/level-order-tree-traversal/
# breadth first traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_level_order(root):
    if root is None:
        return None
    queue = []

    queue.append(root)

    while (len(queue) > 0):
    
        print (queue[0].data)
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)



root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print_level_order(root)
