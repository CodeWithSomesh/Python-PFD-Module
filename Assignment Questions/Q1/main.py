import os
from smartphone import Smartphone
from bst import BST

def addPhone(bst):

    try:
        productCode = (input("\nEnter Product Code: ")).upper()
        brand = input("Enter Phone Brand: ")
        model = input("Enter Phone Model: ")
        sellingPrice = float(input("Enter Phone Selling Price: RM"))
        color = input("Enter Phone Color: ")
        quantityOnHand = int(input("Enter Quantity: "))
        serialNumber = input("Enter Serial Number: ")
        newPhone = Smartphone(productCode, brand, model, sellingPrice, color, quantityOnHand, serialNumber)
        bst.addChild(newPhone, bst.root)
        print("\nProduct added successfully.")
        print("\nNew Product Details: ")
        print(newPhone)
    except ValueError as e:
        print(f"Invalid input: {e}")

def viewAllPhones(bst):

    allPhones = bst.inOrderTraversal(bst.root)
    if allPhones is None:
        print("\nThere aren't any products added in the system")
    else:
        for phones in allPhones:
            print(f"\n{phones}")

def searchPhoneByProductCode(bst):
    productCode = (input("\nEnter Product Code to search: ")).upper()
    foundPhone = bst.search(productCode, bst.root)
    # print(foundPhone)
    print()
    if foundPhone:
        print(foundPhone)
    else:
        print("No phone found for the given Product Code.")

def searchPhonesByBrand(bst):
    foundPhones = []
    brand = input("\nEnter Phone Brand to search: ")
    allPhones = bst.inOrderTraversal(bst.root)

    for phones in allPhones:
        if brand.lower() == phones.brand.lower():
            foundPhones.append(phones)

    print()
    if len(foundPhones) == 0:
        print("No phones found for the given Phone Brand.")
    else:
        for phones in foundPhones:
            print(phones)

def modifyPhoneDetails(bst):
    productCode = (input("\nEnter Product Code to modify: ")).upper()
    existingPhone = bst.search(productCode, bst.root)
    print()
    if not existingPhone:
        print("Product not found.")
        return
    print("Current phone details:")
    print(existingPhone)
    print()
    print("Enter new details (leave blank and press enter to keep existing value):")
    brand = input(f"Enter Brand ({existingPhone.brand}): ") or existingPhone.brand
    model = input(f"Enter Model ({existingPhone.model}): ") or existingPhone.model
    sellingPrice = input(f"Enter Selling Price ({existingPhone.sellingPrice}): RM")
    sellingPrice = float(sellingPrice) if sellingPrice else existingPhone.sellingPrice
    color = input(f"Enter Color ({existingPhone.color}): ") or existingPhone.color
    quantityOnHand = input(f"Enter Quantity ({existingPhone.quantityOnHand}): ")
    quantityOnHand = int(quantityOnHand) if quantityOnHand else existingPhone.quantityOnHand
    serialNumber = input(f"Enter Serial Number ({existingPhone.serialNumber}): ") or existingPhone.serialNumber
    newPhoneDetails = Smartphone(productCode, brand, model, sellingPrice, color, quantityOnHand, serialNumber)
    # print(newPhoneDetails)
    modifiedPhone = bst.modify(productCode, newPhoneDetails)
    print("\nProduct details updated successfully.")
    print("\nNewly modified phone details:")
    print(modifiedPhone)



def menu(bst):
    while True:
        print("\nWelcome To Switch Store Stock Management System")
        print("\nAvailable Operations: ")
        print("1. Create a new product")
        print("2. View all products")
        print("3. Search for a phone by product code")
        print("4. Search for a phone by phone brand")
        print("5. Modify phone details")
        print("6. Exit")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            os.system('cls')
            print("Create a new product: ")
            addPhone(bst)
            print()
            os.system('pause')
            os.system('cls')
        elif choice == '2':
            os.system('cls')
            print("View all products: ")
            viewAllPhones(bst)
            print()
            os.system('pause')
            os.system('cls')
        elif choice == '3':
            os.system('cls')
            print("Search for a phone by product code: ")
            searchPhoneByProductCode(bst)
            print()
            os.system('pause')
            os.system('cls')
        elif choice == '4':
            os.system('cls')
            print("Search for a phone by phone brand: ")
            searchPhonesByBrand(bst)
            print()
            os.system('pause')
            os.system('cls')
        elif choice == '5':
            os.system('cls')
            print("Modify phone details: ")
            modifyPhoneDetails(bst)
            print()
            os.system('pause')
            os.system('cls')
        elif choice == '6':
            print("Exiting the system. Have a goo day!")
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
