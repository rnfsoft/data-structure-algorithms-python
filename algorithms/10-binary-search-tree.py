class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        root = Node(data)
    elif data <= root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root



def search(root, data):
    if root == None:
        return False
    elif root.data == data:
        return root
    elif data <= root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)


def delete(root, data):
    if root is None:
        return root
    if data == root.data:
        if root.left and root.right:
            parent, child = root, root.right
            while child.left:
                parent, child = child, child.left
            child.left = root.left
            if parent != root:
                parent.left = child.right
                child.right = root.right
            root = child
        elif root.left or root.right:
            root = root.left or root.right
        else:
            root = None
    elif data < root.data:
        root.left = delete(root.left, data)
    else:
        root.right = delete(root.right, data)
    return root
                

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)
# inorder(root)
#print ("Found" if search(root, 31) else "Not Found")
root = delete(root, 20)
root = delete(root, 30)
root = delete(root, 50)
inorder(root)


