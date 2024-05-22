import os

class Product:
    def __init__(self, product_code, brand, model, selling_price, color, quantity, serial_number):
        self.product_code = product_code
        self.brand = brand
        self.model = model
        self.selling_price = selling_price
        self.color = color
        self.quantity = quantity
        self.serial_number = serial_number

    def __str__(self):
        return (f"Product Code: {self.product_code}, Brand: {self.brand}, Model: {self.model}, "
                f"Selling Price: RM{self.selling_price}, Color: {self.color}, "
                f"Quantity: {self.quantity}, Serial Number: {self.serial_number}")

class BSTNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, product):
        if self.root is None:
            self.root = BSTNode(product)
        else:
            self._insert(self.root, product)

    def _insert(self, node, product):
        if product.product_code < node.product.product_code:
            if node.left is None:
                node.left = BSTNode(product)
            else:
                self._insert(node.left, product)
        elif product.product_code > node.product.product_code:
            if node.right is None:
                node.right = BSTNode(product)
            else:
                self._insert(node.right, product)
        else:
            print("Product with this code already exists.")

    def search(self, product_code):
        return self._search(self.root, product_code)

    def _search(self, node, product_code):
        if node is None:
            return None
        if product_code == node.product.product_code:
            return node.product
        elif product_code < node.product.product_code:
            return self._search(node.left, product_code)
        else:
            return self._search(node.right, product_code)

    def inorder_traversal(self, node, result):
        if node is not None:
            self.inorder_traversal(node.left, result)
            result.append(node.product)
            self.inorder_traversal(node.right, result)

    def modify(self, product_code, new_product): #There is some problem with this function
        node = self._search(self.root, product_code)
        if node:
            node.product = new_product
        else:
            print("Product not found.")

class StockManagementSystem:
    def __init__(self):
        self.bst = BST()

    def create_product(self):
        try:
            product_code = input("Enter Product Code: ")
            brand = input("Enter Brand: ")
            model = input("Enter Model: ")
            selling_price = float(input("Enter Selling Price: "))
            color = input("Enter Color: ")
            quantity = int(input("Enter Quantity: "))
            serial_number = input("Enter Serial Number: ")
            new_product = Product(product_code, brand, model, selling_price, color, quantity, serial_number)
            self.bst.insert(new_product)
            print("Product added successfully.")
        except ValueError as e:
            print(f"Invalid input: {e}")

    def view_all_products(self):
        products = []
        self.bst.inorder_traversal(self.bst.root, products)
        if not products:
            print("No products in the stock.")
        else:
            for product in products:
                print(product)

    def search_product(self):
        brand = input("Enter Brand to search: ")
        products = []
        self.bst.inorder_traversal(self.bst.root, products)
        found_products = [product for product in products if product.brand.lower() == brand.lower()]
        if not found_products:
            print("No products found for the given brand.")
        else:
            for product in found_products:
                print(product)

    def modify_product(self):
        product_code = input("Enter Product Code to modify: ")
        existing_product = self.bst.search(product_code)
        if not existing_product:
            print("Product not found.")
            return
        print("Current product details:")
        print(existing_product)
        print("Enter new details (leave blank to keep current value):")
        brand = input(f"Enter Brand ({existing_product.brand}): ") or existing_product.brand
        model = input(f"Enter Model ({existing_product.model}): ") or existing_product.model
        selling_price = input(f"Enter Selling Price ({existing_product.selling_price}): RM")
        selling_price = float(selling_price) if selling_price else existing_product.selling_price
        color = input(f"Enter Color ({existing_product.color}): ") or existing_product.color
        quantity = input(f"Enter Quantity ({existing_product.quantity}): ")
        quantity = int(quantity) if quantity else existing_product.quantity
        serial_number = input(f"Enter Serial Number ({existing_product.serial_number}): ") or existing_product.serial_number
        new_product = Product(product_code, brand, model, selling_price, color, quantity, serial_number)
        print(new_product)
        self.bst.modify(product_code, new_product)
        print("Product details updated successfully.")


    def menu(self):
        while True:
            print("\n1. Create a new product")
            print("2. View all products")
            print("3. Search for a product by brand")
            print("4. Modify product details")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.create_product()
            elif choice == '2':
                self.view_all_products()
            elif choice == '3':
                self.search_product()
            elif choice == '4':
                self.modify_product()
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                input("Press Enter to continue...")


if __name__ == "__main__":
    system = StockManagementSystem()
    system.menu()
