class Node:
    def __init__(self, parent, name, path):
        self.name = name
        self.path = path
        self.left = None
        self.right = None
        if parent: parent.add_child(self)
    def add_child(self, child):
        if not self.left:
            self.left = child
            return
        self.left.add_sibling(child)
    def add_sibling(self, sibling):
        if not self.right:
            self.right = sibling
            return
        self.right.add_sibling(sibling)

class BinaryTree:
    def __init__(self):
        self.root = Node(None, 'root', '.')
        self.whiteList = []

    def add_node(self, parent, name, path):
        return Node(parent, name, path)

    def preorder(self, root, level=0):
        if root.path in self.whiteList: print("-"*4*level + "\033[1m" + root.name + "\033[0m")
        else: print("-"*4*level + root.name)
        if root.left: self.preorder(root.left, level+1)
        if root.right: self.preorder(root.right, level)
    
    def print_tree(self, whiteList):
        self.whiteList = whiteList 
        self.preorder(self.root)