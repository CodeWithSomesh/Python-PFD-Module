# Creating a Node of a BST
class Node:
    # Constructor
    # Defining the components of the ROOT Node, with the Data, Right Child and Left Child
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    # Constructor
    # Root Node will be set
    def __init__(self, data):
        self.root = Node(data)

    def search(self, node, value):

        if node.data == value:
            return True

        if value < node.data:

            if node.left:
                return self.search(node.left, value)
            else:
                return False

        if value > node.data:

            if node.right:
                return self.search(node.right, value)
            else:
                return False


    # this functions adds a node based on the principles of BST,
    # left nodes values are smaller than root node, vice versa
    def addChild(self, node,  data):
        # check if got repeated value, if got return nothing
        if data == node.data:
            return

        # check if PARAMETER data is lesser than NODE data
        if data < node.data:
            # if there is already a left node then run addChild function recursively, until it finds an empty left node
            if node.left:
                self.addChild(node.left, data)
            # if there is an empty left node, then create a new node using BST Class
            else:
                node.left = Node(data)

        if data > node.data:
            # Check if there are any existing right node,
            # if there are then keep finding for an empty right node recursively
            if node.right:
                self.addChild(node.right, data)
            # if there is an empty right node, then create a new node using BST Class
            else:
                node.right = Node(data)

    # Using LVR to return an array of numbers/elements
    def inOrderTraversal(self, node):
        #Initialize empty array
        elements = []

        # vist Left node first, then recursively find for the furthest left leaf node,
        # then add in the array
        if node.left:
            elements += self.inOrderTraversal(node.left)

        # After adding the left node value of the node, then add the root node value
        elements.append(node.data)

        # Lastly add the right node recursively
        if node.right:
            elements += self.inOrderTraversal(node.right)

        return elements

    # Using VLR to return an array of numbers/elements
    def preOrderTraversal(self, node):
        #Initialize empty array
        elements = []

        # First add the root node value
        elements.append(node.data)

        # vist Left node, then recursively find for the furthest left leaf node,
        # then add in the array
        if node.left:
            elements += self.preOrderTraversal(node.left)

        # vist right  node, then recursively find for the furthest left leaf node,
        # then add in the array
        if node.right:
            elements += self.preOrderTraversal(node.right)

        return elements

    # Using LRV to return an array of numbers/elements
    def postOrderTraversal(self, node):
        #Initialize empty array
        elements = []

        # vist Left node, then recursively find for the furthest left leaf node,
        # then add in the array
        if node.left:
            elements += self.postOrderTraversal(node.left)

        # vist right  node, then recursively find for the furthest left leaf node,
        # then add in the array
        if node.right:
            elements += self.postOrderTraversal(node.right)

        # Lastly add the root node value
        elements.append(node.data)

        return elements

    # Find the highest value of the BST, which is always on the right side of the tree,
    # the last node on the right is always the biggest
    def findMax(self, node):

        if node.right is None:
            return node.data

        return self.findMax(node.right)

    # Find the lowest value of the BST, which is always on the left side of the tree,
    # the last node on the left is always the smallest
    def findMin(self, node):

        if node.left is None:
            return node.data

        return self.findMin(node.left)

if __name__ == "__main__":

    numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    # Initialize the root of the BST
    root = Node(numbers[0])

    numbers_tree = BST(root)

    for i in range(1, len(numbers)):
        numbers_tree.addChild(root, numbers[i])

    print(numbers_tree.findMin(root))


