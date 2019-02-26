"""Basic Coding example on implementing a BST"""


class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.value = key


# Function to insert to the binary tree
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value > node.value:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)


# Function to search for a key  if present in the BST
def lookup(root, key):
    if root is None or root.value == key:
        return root

    if root.value > key:
        return lookup(root.left, key)
    else:
        return lookup(root.right, key)


# function to output the BST in order
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


# function to output the BST post order
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)


# function to output the BST pre order
def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        postorder(root.right)


bt = Node(50)
insert(bt, Node(30))
insert(bt, Node(20))
insert(bt, Node(40))
insert(bt, Node(70))
insert(bt, Node(60))
insert(bt, Node(80))

print("In-Order: ")
print(inorder(bt))
print("Post-Order: ")
print(postorder(bt))
print("Pre Order: ")
print(preorder(bt))


