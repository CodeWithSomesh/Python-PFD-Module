class Smartphone:
    # Constructor
    # Initializing phones, all nodes originally have all these attributes
    def __init__(self, productCode, brand, model, sellingPrice, colorArray,  quantityOnHandArray, serialNumber):
        self.productCode = productCode
        self.brand = brand
        self.model = model
        self.sellingPrice = sellingPrice
        self.colorArray = colorArray
        self.quantityOnHandArray = quantityOnHandArray
        self.serialNumber = serialNumber

    # The __str__ method is called to get a user-friendly string representation of the object
    # Particularly useful for debugging and logging
    def __str__(self):
        allColors = ', '.join(self.colorArray)
        allQuantity = ', '.join(self.quantityOnHandArray)

        return (f"Product Code: {self.productCode}, Brand: {self.brand}, Model: {self.model}, "
                f"Selling Price: RM{self.sellingPrice:.2f}, Serial Number: {self.serialNumber}"
                f"\nAll Colors: {allColors} \nAll Quantity: {allQuantity}")

    # Updating details of the phone when user select Modify Choice in Menu
    def updateDetails(self, newPhoneDetails):
        self.productCode = newPhoneDetails.productCode
        self.brand = newPhoneDetails.brand
        self.model = newPhoneDetails.model
        self.sellingPrice = newPhoneDetails.sellingPrice
        self.colorArray = newPhoneDetails.colorArray
        self.quantityOnHandArray = newPhoneDetails.quantityOnHandArray
        self.serialNumber = newPhoneDetails.serialNumber
        return self