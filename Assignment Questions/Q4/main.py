import threading
import os

def calculateMonthlyMortage(customerName, principalAmmount, yearlyInterestRate, totalLoanYears, results):

    yearlyInterestRatePercentage = yearlyInterestRate/100              # Get the percentage of yearly interest rate
    monthlyInterestRatePercentage = yearlyInterestRatePercentage/12    # Get the percentage of monthly interest rate

    # Calculating the upper part of the Monthly Mortage Formula
    formulaUpperPart = principalAmmount * monthlyInterestRatePercentage
    # Calculating the lower part of the Monthly Mortage Formula
    formulaLowerPart = 1 - (1/ ((1 + monthlyInterestRatePercentage) ** (12 * totalLoanYears)))


    monthlyMortage = formulaUpperPart/formulaLowerPart # Calculate monthly mortage using the complete formula
    results[customerName] = {
        "principalAmount": principalAmmount,
        "yearlyInterestRate": yearlyInterestRate,
        "tenure": totalLoanYears,
        "monthlyMortage": f"{monthlyMortage:.2f}"
    }

def displayResults(results):
    for customerName, details in results.items():
        principalAmount = details["principalAmount"]
        interestRate = details["yearlyInterestRate"]
        tenure = details["tenure"]
        mortageAmount = details["monthlyMortage"]

        print("*" * 60)
        print(f"Customer Name: {customerName}")
        print(f"Principal Amount: {principalAmount}")
        print(f"Interest Rate: {interestRate}")
        print(f"Loan Tenure: {tenure}")

        print("-" * 45)
        print(f"{customerName}'s monthly mortgage is: RM{mortageAmount}")
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
        threads.append(threading.Thread(target=calculateMonthlyMortage,
                                        args=(customerName, principalAmount, interestRate, tenure, results)))
        threads[-1].start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    displayResults(results)



def main():

    while True:
        print("\nWelcome To Switch Store Stock Management System")
        print("\nAvailable Operations: ")
        print("1. Calculate the monthly mortgage repayment for 3 different customers using existing data")
        print("2. Calculate the monthly mortgage repayment for however many people you want to")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            os.system('cls')
            print("Create a new product: ")
            displayExistingData()
            print()
            os.system('pause')
            os.system('cls')
        elif choice == '2':
            os.system('cls')
            print("View all products: ")
            # viewAllPhones(bst)
            print()
            os.system('pause')
            os.system('cls')




if __name__ == "__main__":
    main()


