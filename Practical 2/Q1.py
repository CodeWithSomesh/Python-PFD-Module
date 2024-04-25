class BST:
    # Constructor
    # Defining the components of the ROOT Node, with the Data, Right Child and Left Child
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    # this functions adds a node based on the principles of BST,
    # left nodes values are smaller than root node, vice versa
    def addChild(self, data):
        # check if got repeated value, if got return nothing
        if data == self.data:
            return

        # check if PARAMETER data is lesser than NODE data
        if data < self.data:
            # if there is already a left node then run addChild function recursively, until it finds an empty left node
            if self.left:
                self.left.addChild(data)
            # if there is an empty left node, then create a new node using BST Class
            else:
                self.left = BST(data)

        if data > self.data:
            # Check if there are any existing right node,
            # if there are then keep finding for an empty right node recursively
            if self.right:
                self.right.addChild(data)
            # if there is an empty right node, then create a new node using BST Class
            else:
                self.right = BST(data)

    # Using LVR to return an array of numbers/elements
    def inOrderTraversal(self):
        #Initialize empty array
        elements = []

        # vist Left node first, then recursively find for the furthest left leaf node,
        # then add in the array
        if self.left:
            elements += self.left.inOrderTraversal()

        # After adding the left node value of the node, then add the root node value
        elements.append(self.data)

        # Lastly add the right node recursively
        if self.right:
            elements += self.right.inOrderTraversal()

        return elements

    # Using VLR to return an array of numbers/elements
    def preOrderTraversal(self):
        #Initialize empty array
        elements = []

        # First add the root node value
        elements.append(self.data)

        # vist Left node, then recursively find for the furthest left leaf node,
        # then add in the array
        if self.left:
            elements += self.left.preOrderTraversal()

        # vist right  node, then recursively find for the furthest left leaf node,
        # then add in the array
        if self.right:
            elements += self.right.preOrderTraversal()

        return elements

    # Using LRV to return an array of numbers/elements
    def postOrderTraversal(self):
        #Initialize empty array
        elements = []

        # vist Left node, then recursively find for the furthest left leaf node,
        # then add in the array
        if self.left:
            elements += self.left.postOrderTraversal()

        # vist right  node, then recursively find for the furthest left leaf node,
        # then add in the array
        if self.right:
            elements += self.right.postOrderTraversal()

        # Lastly add the root node value
        elements.append(self.data)

        return elements

def buildTree(elements):
    # Initialize the root of the BST
    root = BST(elements[0])

    for i in range(1, len(elements)):
        root.addChild(elements[i])

    return root

if __name__ == "__main__":

    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = buildTree(numbers)
    print(numbers_tree.postOrderTraversal())


