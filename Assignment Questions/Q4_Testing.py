# <<<<<<<<<<<<<<<<<<<<<<< My Method >>>>>>>>>>>>>>>>>>>>>>>>>>>>
def calculateMonthlyMortage(principal, yearlyInterestRate, totalLoanYears, paymentsPerYear):

    yearlyInterestRatePercentage = yearlyInterestRate/100              # Get the percentage of yearly interest rate
    monthlyInterestRatePercentage = yearlyInterestRatePercentage/12    # Get the percentage of monthly interest rate


    formulaUpperPart = principal * monthlyInterestRatePercentage
    formulaLowerPart = 1 - (1/ ((1 + monthlyInterestRatePercentage) ** (paymentsPerYear * totalLoanYears)))


    monthlyMortage = formulaUpperPart/formulaLowerPart
    return monthlyMortage


# <<<<<<<<<<<<<<<<<<<<<<< GPT Method >>>>>>>>>>>>>>>>>>>>>>>>>>>>
def calculate_monthly_repayment(principal, annual_interest_rate, loan_term_years):
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = annual_interest_rate / 100 / 12
    # Total number of monthly payments
    number_of_payments = loan_term_years * 12

    if monthly_interest_rate == 0:
        # If interest rate is 0, simply divide the principal by the number of payments
        monthly_repayment = principal / number_of_payments
    else:
        # Calculate the monthly repayment using the formula
        monthly_repayment = (
                        principal * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments
                    ) / ((1 + monthly_interest_rate) ** number_of_payments - 1)

    return monthly_repayment


principal = 200000.00
yearlyInterestRate = 4.5
totalLoanYears = 30
paymentsPerYear = 12

# My formula
monthlyMortage1 =calculateMonthlyMortage(principal, yearlyInterestRate, totalLoanYears, paymentsPerYear)

# GPT formula
monthlyMortage2 =calculate_monthly_repayment(principal, yearlyInterestRate, totalLoanYears)


print(monthlyMortage1)
print(monthlyMortage2)
