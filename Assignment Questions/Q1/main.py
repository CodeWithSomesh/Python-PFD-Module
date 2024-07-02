import random
import os
from smartphone import Smartphone
from bst import BST

def getFloatInput(prompt, existingPhone=None):
    while True:
        userInput = input(prompt) or existingPhone.sellingPrice
        try:
            # Try to convert the input to a float
            num = float(userInput)
            return num

        except ValueError:
            # If conversion fails, it's not a valid number
            print("Invalid input. Please enter a valid number.")


def getIntInput(prompt):
    while True:
        userInput = input(prompt)
        if userInput.isdigit():
            return int(userInput)
        else:
            print("Invalid input. Please enter a valid integer number.")

def getYesOrNoInput(prompt):
    while True:
        userInput = input(prompt).upper()
        if userInput == 'Y' or userInput == 'YES':
            return True
        elif userInput == 'N' or userInput == 'NO':
            return False
        else:
            print("Invalid input. Please enter 'Yes' or 'No' only.")


def addPhone(bst):
    colorArray = []
    quantityArray = []


    productCode = (input("\nEnter Product Code: ")).upper()
    allPhones = bst.inOrderTraversal(bst.root)
    if allPhones is not None:
        for phones in allPhones:
            if productCode == phones.productCode:
                print("\nThere is already a phone under this Product Code.")
                print("Select 1 in the Menu to add a new phone with a different Product Code.")
                print("Select 5 in the Menu to modify the details of the phone with this Product Code.")
                return


    serialNumber = input("Enter Serial Number: ")
    brand = input("Enter Phone Brand: ")
    model = input("Enter Phone Model: ")
    sellingPrice = getFloatInput("Enter Phone Selling Price: RM")

    numberOfColors = getIntInput("Enter Number of Colorways Available: ")
    for i in range(numberOfColors):
        color = input(f"Enter Phone Color {i+1}: ")
        quantityOnHand = getIntInput(f"Enter Quantity of Phone Color {i+1}: ")
        quantityOnHand = str(quantityOnHand)
        colorArray.append(color)
        quantityArray.append(quantityOnHand)

    newPhone = Smartphone(productCode, brand, model, sellingPrice, colorArray, quantityArray, serialNumber)
    bst.addChild(newPhone, bst.root)
    print("\nProduct added successfully.")
    print("\nNew Product Details: ")
    print(newPhone)


def viewAllPhones(bst):
    num = 1
    allPhones = bst.inOrderTraversal(bst.root) # Displaying starting from the smallest Product Code
    if allPhones is None:
        print("\nThere aren't any products added in the system")
    else:
        for phones in allPhones:
            print(f"\n******************** Product {num} ******************** ")
            print(f"{phones}")
            num += 1

def searchPhoneByProductCode(bst):
    allPhones = bst.inOrderTraversal(bst.root)
    if allPhones is None:
        print("\nThere aren't any products added in the system")
        return

    displayAvailableProductCodes(bst)

    productCode = (input("\nEnter Product Code to search: ")).upper()
    foundPhone = bst.search(productCode, bst.root)
    print()

    if foundPhone:
        print(foundPhone)
    else:
        print("No phone found for the given Product Code.")

def searchPhonesByBrand(bst):
    foundPhones = []
    num = 1

    allPhones = bst.inOrderTraversal(bst.root)
    if allPhones is None:
        print("\nThere aren't any products added in the system")
        return

    displayAvailableProductBrands(bst)

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
            print(f"\n******************** Product {num} ******************** ")
            print(f"{phones}")
            num += 1

def modifyPhoneDetails(bst):
    colorArray = []
    quantityArray = []


    allPhones = bst.inOrderTraversal(bst.root)
    if allPhones is None:
        print("\nThere aren't any products added in the system")
        return

    displayAvailableProductCodes(bst)

    productCode = (input("\nEnter Product Code to modify: ")).upper()
    existingPhone = bst.search(productCode, bst.root)
    print()

    if not existingPhone:
        print("Product not found.")
        return

    print("Current phone details:")
    print(existingPhone)
    print()

    print("Enter new details (Leave blank and Press Enter to keep existing value):")
    serialNumber = input(f"Enter Serial Number ({existingPhone.serialNumber}): ") or existingPhone.serialNumber
    brand = input(f"Enter Brand ({existingPhone.brand}): ") or existingPhone.brand
    model = input(f"Enter Model ({existingPhone.model}): ") or existingPhone.model
    sellingPrice = getFloatInput(f"Enter Selling Price (RM{existingPhone.sellingPrice:.2f}): RM", existingPhone)
    # sellingPrice = float(sellingPrice) if sellingPrice else existingPhone.sellingPrice  # Need make changes
    askToModify = getYesOrNoInput("Do you want to modify the Phone Color and Quantity? (Yes/No): ")

    if askToModify:
        numberOfColors = getIntInput("Enter Number of Colorways Available: ")
        for i in range(numberOfColors):
            color = input(f"Enter Phone Color {i + 1}: ")
            quantityOnHand = getIntInput(f"Enter Quantity of Phone Color {i + 1}: ")
            quantityOnHand = str(quantityOnHand)
            colorArray.append(color)
            quantityArray.append(quantityOnHand)
    else:
        colorArray = existingPhone.colorArray
        quantityArray = existingPhone.quantityOnHandArray



    newPhoneDetails = Smartphone(productCode, brand, model, sellingPrice, colorArray, quantityArray, serialNumber)
    modifiedPhone = bst.modify(productCode, newPhoneDetails)
    print("\nProduct details updated successfully.")
    print("\nNewly modified phone details:")
    print(modifiedPhone)


def displayAvailableProductCodes(bst):
    num = 1
    allPhones = bst.inOrderTraversal(bst.root)  # Displaying starting from the smallest Product Code
    if allPhones is None:
        print("\nThere aren't any products added in the system")
    else:
        print(f"\n******************** Available Product Codes In The System ********************* ")

        for phones in allPhones:
            print(f"{num}. {phones.productCode}")
            num += 1

        print("*" * 80)


def displayAvailableProductBrands(bst):
    num = 1
    allPhones = bst.inOrderTraversal(bst.root)  # Displaying starting from the smallest Product Code
    if allPhones is None:
        print("\nThere aren't any products added in the system")
    else:
        print(f"\n******************** Available Phone Brands In The System ********************* ")

        for phones in allPhones:
            print(f"{num}. {phones.brand}")
            num += 1

        print("*" * 80)

def menu(bst):
    while True:
        print("\nWelcome To Switch Store Stock Management System")
        print("\nAvailable Operations: ")
        print("1. Create a new product")
        print("2. View all products")
        print("3. Search for a phone by product code")
        print("4. Search for phones by phone brand")
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
            print("Search for phones by phone brand: ")
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
            os.system('cls')
            print("Exiting the system. Have a good day!")
            print()
            os.system('pause')
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            os.system('pause')
            os.system('cls')

def main():
    bst = BST()
    menu(bst)


if __name__ == "__main__":
    main()
