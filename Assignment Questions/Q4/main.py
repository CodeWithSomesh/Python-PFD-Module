import threading
import os

# Function that ensures the inputs are float variable and more than 0
def getFloatInput(prompt):
    while True:
        userInput = input(prompt)
        try:
            # Try to convert the input to a float
            num = float(userInput)

            if num < 1:
                print("Invalid input. Please enter a number that is at least 1 or higher.\n")
                continue

            return num


        except ValueError:
            # If conversion fails, it's not a valid number
            print("Invalid input. Please enter a valid number.\n")


# Function that ensures the inputs are int variable and more than 0
def getIntInput(prompt):
    while True:
        userInput = input(prompt)
        if userInput.isdigit():
            return int(userInput)
        else:
            print("Invalid input. Please enter a valid and positive integer number.\n")


def calculateMonthlyMortgage(customerName, principalAmount, yearlyInterestRate, totalLoanYears, results):

    yearlyInterestRatePercentage = yearlyInterestRate/100              # Get the percentage of yearly interest rate
    monthlyInterestRatePercentage = yearlyInterestRatePercentage/12    # Get the percentage of monthly interest rate

    # Calculating the upper part of the Monthly Mortgage Formula
    formulaUpperPart = principalAmount * monthlyInterestRatePercentage
    # Calculating the lower part of the Monthly Mortgage Formula
    formulaLowerPart = 1 - (1/ ((1 + monthlyInterestRatePercentage) ** (12 * totalLoanYears)))


    monthlyMortgage = formulaUpperPart/formulaLowerPart # Calculate monthly mortgage using the complete formula

    # Creating an object for results with customer details
    results[customerName] = {
        "principalAmount": principalAmount,
        "yearlyInterestRate": yearlyInterestRate,
        "tenure": totalLoanYears,
        "monthlyMortgage": f"{monthlyMortgage:.2f}"
    }


def displayResults(results):
    print()
    for customerName, details in results.items():
        principalAmount = details["principalAmount"]
        interestRate = details["yearlyInterestRate"]
        tenure = details["tenure"]
        mortgageAmount = details["monthlyMortgage"]

        print("*" * 60)
        print(f"Customer Name: {customerName}")
        print(f"Principal Amount: RM{principalAmount}")
        print(f"Interest Rate: {interestRate}%")
        print(f"Loan Tenure: {tenure} Years")

        print("-" * 45)
        print(f"{customerName}'s monthly mortgage is: RM{mortgageAmount}")
        print("-" * 45)

        print("*" * 60)
        print()


def displayExistingData():
    # Initialize Variables
    results = {}
    threads = []

    # Define the loan details for the 3 customers
    customers = {
        "Somesh": {
            "principalAmount": 100000,
            "interestRate": 4.5,
            "tenure": 15
        },
        "Weng Kean": {
            "principalAmount": 200000,
            "interestRate": 4.5,
            "tenure": 30
        },
        "Jun Khai": {
            "principalAmount": 300000,
            "interestRate": 4.5,
            "tenure": 20
        }
    }

    # Create and start a thread for each customer

    for customerName, details in customers.items():
        principalAmount = details["principalAmount"]
        interestRate = details["interestRate"]
        tenure = details["tenure"]

        # Create a thread for each customer
        threads.append(threading.Thread(target=calculateMonthlyMortgage,
                                        args=(customerName, principalAmount, interestRate, tenure, results)))
        threads[-1].start() # Start the thread

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    displayResults(results)


def displayBasedOnUserInput():
    # Initialize Variables
    results = {}
    threads = []

    numberOfCustomers = getIntInput("\nEnter Number of Customers: ") # Asking customer number

    for i in range(numberOfCustomers): # Looping through entered number
        print("-" * 70)
        customerName = input(f'Enter Customer {i + 1} Name: ')
        principalAmount = getFloatInput(f"Enter {customerName}'s Loan Principal Amount: RM")
        interestRate = getFloatInput(f"Enter {customerName}'s Loan Annual Interest Rate (1% to 100%): ")
        tenure = getIntInput(f"Enter {customerName}'s Loan Tenure: ")

        # Create a thread for each customer
        threads.append(threading.Thread(target=calculateMonthlyMortgage,
                                        args=(customerName, principalAmount, interestRate, tenure, results)))
        threads[-1].start()  # Start the thread

        print("-" * 70)
        print()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    os.system('pause')
    os.system('cls')
    displayResults(results)


def main():
    results = {}

    while True:
        print("\nWelcome To Mortgage Calculating System")
        print("\nAvailable Operations: ")
        print("1. Calculate the monthly mortgage repayment for 3 predefined customers")
        print("2. Calculate the monthly mortgage repayment for any number of customers (Enter data manually)")
        print("3. Exit")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            os.system('cls')
            print("Calculate the monthly mortgage repayment for 3 predefined customers: ")
            displayExistingData()
            os.system('pause')
            os.system('cls')
        elif choice == '2':
            os.system('cls')
            print("Calculate the monthly mortgage repayment for any number of customers (Enter data manually): ")
            displayBasedOnUserInput()
            print()
            os.system('pause')
            os.system('cls')
        elif choice == '3':
            os.system('cls')
            print("Exiting the system. Have a good day!")
            print()
            os.system('pause')
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            os.system('pause')
            os.system('cls')




if __name__ == "__main__":
    main()


