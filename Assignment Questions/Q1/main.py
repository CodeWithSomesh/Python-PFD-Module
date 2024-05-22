import os
from smartphone import Smartphone
from bst import BST

def addPhone(bst):

    try:
        productCode = input("Enter Product Code: ")
        brand = input("Enter Phone Brand: ")
        model = input("Enter Phone Model: ")
        sellingPrice = float(input("Enter Phone Selling Price: RM"))
        color = input("Enter Phone Color: ")
        quantityOnHand = int(input("Enter Quantity: "))
        serialNumber = input("Enter Serial Number: ")
        newPhone = Smartphone(productCode, brand, model, sellingPrice, color, quantityOnHand, serialNumber)
        bst.addChild(newPhone, bst.root)
        print("Product added successfully.")
    except ValueError as e:
        print(f"Invalid input: {e}")

def viewAllPhones(bst):

    allPhones = bst.inOrderTraversal(bst.root)
    if allPhones is None:
        print("There aren't any products added in the system")
    else:
        for phones in allPhones:
            print(phones)

def searchPhoneByProductCode(bst):
    productCode = input("Enter Product Code to search: ")
    foundPhone = bst.search(productCode, bst.root)
    # print(foundPhone)
    if foundPhone:
        print(foundPhone)
    else:
        print("No phone found for the given Product Code.")

def searchPhonesByBrand(bst):
    foundPhones = []
    brand = input("Enter Phone Brand to search: ")
    allPhones = bst.inOrderTraversal(bst.root)

    for phones in allPhones:
        if brand.lower() == phones.brand.lower():
            foundPhones.append(phones)

    if len(foundPhones) == 0:
        print("No phone found for the given Phone Brand.")
    else:
        for phones in foundPhones:
            print(phones)

def modifyPhoneDetails(bst):
    productCode = input("Enter Product Code to modify: ")
    existingPhone = bst.search(productCode, bst.root)
    if not existingPhone:
        print("Product not found.")
        return
    print("Current phone details:")
    print(existingPhone)
    print("Enter new details (leave blank to keep current value):")
    brand = input(f"Enter Brand ({existingPhone.brand}): ") or existingPhone.brand
    model = input(f"Enter Model ({existingPhone.model}): ") or existingPhone.model
    sellingPrice = input(f"Enter Selling Price ({existingPhone.sellingPrice}): RM")
    sellingPrice = float(sellingPrice) if sellingPrice else existingPhone.sellingPrice
    color = input(f"Enter Color ({existingPhone.color}): ") or existingPhone.color
    quantityOnHand = input(f"Enter Quantity ({existingPhone.quantityOnHand}): ")
    quantityOnHand = int(quantityOnHand) if quantityOnHand else existingPhone.quantityOnHand
    serialNumber = input(f"Enter Serial Number ({existingPhone.serialNumber}): ") or existingPhone.serialNumber
    newPhoneDetails = Smartphone(productCode, brand, model, sellingPrice, color, quantityOnHand, serialNumber)
    print(newPhoneDetails)
    bst.modify(productCode, newPhoneDetails)
    print("Product details updated successfully.")



def menu(bst):
    while True:
        print("\n1. Create a new product")
        print("2. View all products")
        print("3. Search for a product by product code")
        print("4. Search for a product by brand")
        print("5. Modify product details")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            addPhone(bst)
        elif choice == '2':
            viewAllPhones(bst)
        elif choice == '3':
            searchPhoneByProductCode(bst)
        elif choice == '4':
            searchPhonesByBrand(bst)
        elif choice == '5':
            modifyPhoneDetails(bst)
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            input("Press Enter to continue...")
            # Clearing the Screen
            os.system('cls')

def main():
    bst = BST()
    menu(bst)


if __name__ == "__main__":
    main()
