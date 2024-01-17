import math

# Display options for user
print("Investment - To calculate the amount of interest you'll earn on your investment")
print("Bond - To calculate the amount you'll have to pay on a home loan")

# Get users choice
answer = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Continue based on input
if answer.upper() == "INVESTMENT":
    # Get details for the calculations to proceed
    deposit = int(input("How much money are you depositing: "))
    interest_rate = int(input("What is your interest rate(Dont add the %): "))
    years = int(input("How many years do you plan on investing: "))
    interest_type = input("Do you a 'simple' or 'compound' interest: ")
    if interest_type.upper() == "SIMPLE":
        # Calculate using the simple interest formula
        r = interest_rate / 100
        p = deposit
        t = years
        a_simple = p * (1 + r*t)
        print("The total interest you will be paying is: " + str(a_simple))

    elif interest_type.upper() == "COMPOUND":
        # Calculate using the compound interest
        r = interest_rate / 100
        p = deposit
        t = years
        a_compound = p * math.pow((1+r), t)
        print("The total interest you will be paying is: " + str(a_compound))

    else:
        # To make sure user enters correct choice
        print("Invalid choice")

elif answer.upper() == "BOND":
    # Get details to do the bond calculations
    value_of_house = int(input("Please enter the present value of the house: "))
    interest_rate = int(input("What is your interest rate(Dont add the %): "))
    months = int(input("Please enter the number of months you plan to repay the bond: "))
    p = value_of_house
    i = (interest_rate / 100) / 12
    n = months
    # Calculating the bond amount
    repayment = (i * p) / (1 - (1 + i)**(-n))
    print("The total amount you will need to pay each month is:" + str(repayment))

else:
    print("Wrong input")
