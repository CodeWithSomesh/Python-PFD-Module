class Smartphone:
    # Constructor
    # Initializing phones, all nodes originally have all these attributes
    def __init__(self, productCode, brand, model, sellingPrice, color,  quantityOnHand, serialNumber):
        self.productCode = productCode
        self.brand = brand
        self.model = model
        self.sellingPrice = sellingPrice
        self.color = color
        self.quantityOnHand = quantityOnHand
        self.serialNumber = serialNumber

    # The __str__ method is called to get a user-friendly string representation of the object
    # Particularly useful for debugging and logging
    def __str__(self):
        return (f"Product Code: {self.productCode}, Brand: {self.brand}, Model: {self.model}, "
                f"Selling Price: RM{self.sellingPrice}, Color: {self.color}, "
                f"Quantity: {self.quantityOnHand}, Serial Number: {self.serialNumber}")

    def updateDetails(self, newPhoneDetails):
        self.productCode = newPhoneDetails.productCode
        self.brand = newPhoneDetails.brand
        self.model = newPhoneDetails.model
        self.sellingPrice = newPhoneDetails.sellingPrice
        self.color = newPhoneDetails.color
        self.quantityOnHand = newPhoneDetails.quantityOnHand
        self.serialNumber = newPhoneDetails.serialNumber
        return self