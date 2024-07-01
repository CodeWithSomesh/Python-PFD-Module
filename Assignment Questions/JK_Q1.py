class Product:
    def __init__(self, product_code, brand, model, selling_price, color, quantity_on_hand, serial_number):
        self.product_code = product_code
        self.brand = brand
        self.model = model
        self.selling_price = selling_price
        self.color = color
        self.quantity_on_hand = quantity_on_hand
        self.serial_number = serial_number

    def __str__(self):
        return (f"Product Code: {self.product_code}, Brand: {self.brand}, Model: {self.model}, "
                f"Selling Price: {self.selling_price}, Color: {self.color}, Quantity: {self.quantity_on_hand}, "
                f"Serial Number: {self.serial_number}")

    def update_details(self, brand=None, model=None, selling_price=None, color=None, quantity_on_hand=None,
                       serial_number=None):
        if brand is not None:
            self.brand = brand
        if model is not None:
            self.model = model
        if selling_price is not None:
            self.selling_price = selling_price
        if color is not None:
            self.color = color
        if quantity_on_hand is not None:
            self.quantity_on_hand = quantity_on_hand
        if serial_number is not None:
            self.serial_number = serial_number


class TreeNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, product):
        if self.root is None:
            self.root = TreeNode(product)
        else:
            self._insert_recursive(self.root, product)

    def _insert_recursive(self, node, product):
        if product.product_code < node.product.product_code:
            if node.left is None:
                node.left = TreeNode(product)
            else:
                self._insert_recursive(node.left, product)
        else:
            if node.right is None:
                node.right = TreeNode(product)
            else:
                self._insert_recursive(node.right, product)

    def search(self, product_code):
        return self._search_recursive(self.root, product_code)

    def _search_recursive(self, node, product_code):
        if node is None or node.product.product_code == product_code:
            return node
        if product_code < node.product.product_code:
            return self._search_recursive(node.left, product_code)
        else:
            return self._search_recursive(node.right, product_code)

    def inorder_traversal(self):
        products = []
        self._inorder_recursive(self.root, products)
        return products

    def _inorder_recursive(self, node, products):
        if node is not None:
            self._inorder_recursive(node.left, products)
            products.append(node.product)
            self._inorder_recursive(node.right, products)


# Menu-driven interface
def display_menu():
    print("\nSwitch Store Stock Management System")
    print("1. Create a new product")
    print("2. View all products")
    print("3. Search for a product by brand")
    print("4. Modify a product's details")
    print("5. Exit")


def create_product():
    product_code = input("Enter product code: ")
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    selling_price = float(input("Enter selling price: "))
    color = input("Enter color: ")
    quantity_on_hand = int(input("Enter quantity on hand: "))
    serial_number = input("Enter serial number: ")
    return Product(product_code, brand, model, selling_price, color, quantity_on_hand, serial_number)


def search_by_brand(bst, brand):
    products = bst.inorder_traversal()
    return [product for product in products if product.brand.lower() == brand.lower()]


def modify_product(product):
    print("Modify Product Details (leave blank to keep current value):")
    brand = input(f"Enter new brand (current: {product.brand}): ") or product.brand
    model = input(f"Enter new model (current: {product.model}): ") or product.model
    selling_price = input(f"Enter new selling price (current: {product.selling_price}): ")
    color = input(f"Enter new color (current: {product.color}): ") or product.color
    quantity_on_hand = input(f"Enter new quantity on hand (current: {product.quantity_on_hand}): ")
    serial_number = input(f"Enter new serial number (current: {product.serial_number}): ") or product.serial_number
    product.update_details(
        brand=brand,
        model=model,
        selling_price=float(selling_price) if selling_price else None,
        color=color,
        quantity_on_hand=int(quantity_on_hand) if quantity_on_hand else None,
        serial_number=serial_number
    )


def main():
    bst = BST()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            product = create_product()
            bst.insert(product)
            print("Product added successfully.")
        elif choice == '2':
            products = bst.inorder_traversal()
            for product in products:
                print(product)
        elif choice == '3':
            brand = input("Enter the brand to search for: ")
            results = search_by_brand(bst, brand)
            if results:
                for product in results:
                    print(product)
            else:
                print("No products found for the specified brand.")
        elif choice == '4':
            product_code = input("Enter the product code of the product to modify: ")
            node = bst.search(product_code)
            if node:
                modify_product(node.product)
                print("Product details updated successfully.")
            else:
                print("Product not found.")
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

