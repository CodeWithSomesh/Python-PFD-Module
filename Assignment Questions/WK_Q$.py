import threading

# Define the Customer class to represent each customer and their loan details
class Customer:
    def __init__(self, name, principal, yearly_interest_rate, num_of_loan, number_payment_year):
        # Initialize the customer with the provided details
        self.name = name
        self.principal = principal
        self.yearly_interest_rate = yearly_interest_rate
        self.num_of_loan = num_of_loan
        self.number_payment_year = number_payment_year
        self.monthly_payment = None

    # Method to calculate the monthly payment for the loan
    def calculate_monthly_payment(self):
        # Calculate the monthly interest rate
        monthly_interest_rate = (self.yearly_interest_rate / 100) / self.number_payment_year
        # Calculate the total number of payments
        total_num_payment = self.num_of_loan * self.number_payment_year
        # Use the formula to calculate the monthly payment
        self.monthly_payment = (self.principal * monthly_interest_rate) / (1 - (1 / (1 + monthly_interest_rate) ** total_num_payment))

    # Method to display the calculated monthly payment
    def display_monthly_payment(self):
        if self.monthly_payment is not None:
            print(f"Monthly payment for {self.name}: ${round(self.monthly_payment, 2)}")
        else:
            print(f"Monthly payment for {self.name} has not been calculated yet.")

# Define a thread class to calculate monthly payments concurrently
class CustomerThread(threading.Thread):
    def __init__(self, customer):
        threading.Thread.__init__(self)
        self.customer = customer

    def run(self):
        # Call the method to calculate the monthly payment
        self.customer.calculate_monthly_payment()

# Function to gather customer details from the user
def gather_customer_details():
    customers = []

    for i in range(3):
        customer_name = input(f"Enter name of Customer {i + 1}: ")

        print(f"{customer_name}, please enter your loan details")
        print("---------------------------------")

        principal = float(input("Enter principal amount: "))
        yearly_interest_rate = float(input("Enter yearly interest rate: "))
        num_of_loan = float(input("Enter number of years of the loan: "))
        number_payment_year = float(input("Enter the number of payments per year: "))
        print("---------------------------------")

        # Create a new Customer object with the gathered details
        customer = Customer(customer_name, principal, yearly_interest_rate, num_of_loan, number_payment_year)
        customers.append(customer)

    return customers

# Main function to execute the program
def main():
    # Gather customer details
    customers = gather_customer_details()

    threads = []
    # Create and start a thread for each customer to calculate their monthly payment
    for customer in customers:
        thread = CustomerThread(customer)
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Display the monthly payments for all customers
    print("The monthly payments for all customers:")
    for customer in customers:
        customer.display_monthly_payment()

# Entry point of the program
if __name__ == '__main__':
    main()

