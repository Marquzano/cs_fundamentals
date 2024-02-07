# Here we will define a basic binary tree class
# As well as it's common operations

class Node(object):
    # The constructor will take the value and assign it for the node
    def __init__(self, value):
        self.value = value
        # For it's left and right nodes we will keep them as None
        # Until they are later assigned or inserted
        self.left = None
        self.right = None

class BinaryTree(object):
    # For the binary tree constructor all we'll need to do is assign the root node
    def __init__(self, root):
        self.root = Node(root)

    # Helper function to print the tree in the specified traversal type order
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    # Start will be the node that will be updated on every single recursive call of the function
    # Traversal will be string that we print and will also be updated on every recursive call
    def preorder(self, start, traversal):
        """ROOT -> LEFT -> RIGHT"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal


# We can begin defining a tree
# I've opted to doing this in python's IDLE/REPL
# $ python3 -i trees/binary_tree.py