class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    def __init__(self, data):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        # Left rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)
        # Right rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)
        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
    def add(self, keys):
        for x in keys:
            self.root = self.insert(self.root, x)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def search(self, root, value):
        if not root or root.value == value:
            return root

        if root.value < value:
            return self.search(root.right, value)
        return self.search(root.left, value)

    def search_value(self, value):
        return self.search(self.root, value)

    def inorder_traversal(self, root, vals):
        if root:
            self.inorder_traversal(root.left, vals)

            vals.append(root.value)
            self.inorder_traversal(root.right, vals)
        return vals

    def preorder_traversal(self, root, vals):
        if root:
            vals.append(root.value)

            self.preorder_traversal(root.left, vals)
            self.preorder_traversal(root.right, vals)
        return vals

    def postorder_traversal(self, root, vals):
        if root:
            self.postorder_traversal(root.left, vals)

            self.postorder_traversal(root.right, vals)
            vals.append(root.value)
        return vals

def main():
    tree = AVLTree()
    tree.add([10, 20, 30, 40, 50])
    print("Tree after insertion:")
    # In-order traversal to print the tree
    print("Inorder Traversal")
    print(tree.inorder_traversal(tree.root, []))
    print("Preorder Traversal")
    print(tree.preorder_traversal(tree.root, []))
    print("Postorder Traversal")
    print(tree.postorder_traversal(tree.root, []))
    result = tree.search_value(30)
    if result:
        print("Node found")
    else:
        print("Node not found")

if __name__ == "__main__":
    main()

