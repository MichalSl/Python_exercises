def mortgageCalculator():
    
    mortgage = int(input("What's the mortgage amount? "))
    interest_rate = float(input("What's the interest rate in % ? "))
    interest_rate = interest_rate / 100 / 12
    lenght = int(input("How many years of of the mortgage? "))
    lenght_months = lenght * 12
    
    income = int(input("What is your monthly income? "))
    
    monthly_payment = mortgage * ((interest_rate * ((1 + interest_rate)**lenght_months)) / (((1 + interest_rate)**lenght_months) - 1))
    
    print("\nThe monthly payment for this mortgage would be {} dolars.".format(round(monthly_payment,2)))
    
    if monthly_payment > income * 0.28:
        print("It is more than 28% of your monthly income. It is more than you can afford")
    else:
        print("It's less than 28% of your monthly income. You can affor that!")
