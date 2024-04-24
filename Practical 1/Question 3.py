# Define a class called Car. The Car class shall include:
# ▪ Two private attributes model and colour representing the model of the
# car and colour of the car respectively.
# ▪ A constructor that takes data and initialize the model and the color of the
# car.
# ▪ Mutator(setter) and accessor(getter) methods for model and color
# respectively.


# ▪ Write a program to test your class as below:
# o Create a Car object (colour = Silver, model = Honda).
# o Change the value of the colour to Red and model to Proton by
# calling appropriate setter method.
# ▪ Display the colour and model of the car by calling appropriate getter
# method.

class Car:

    # Constructor
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour

    # Setter
    def setModel(self, newModel):
        self.model = newModel

    # Getter
    def getModel(self):
        return self.model

    # Setter
    def setColour(self, newColour):
        self.colour = newColour

    # Getter
    def getColour(self):
        return self.colour

if __name__ == "__main__":

    car1 = Car("Honda", "Silver")
    print(f"Car Model:{car1.model}")
    print(f"Car Colour:{car1.colour}\n")

    carModel = input("Enter New Car Model: ")
    car1.setModel(carModel)
    carColour = input("Enter New Car Colour: ")
    car1.setColour(carColour)

    print(f"\nUpdated Car Model:{car1.getModel()}")
    print(f"Updated Car Colour:{car1.getColour()}")