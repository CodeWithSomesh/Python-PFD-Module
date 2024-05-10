class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree:

    def __init__(self, data):
        self.root = Node(data)

    def insert(self, root, data):
