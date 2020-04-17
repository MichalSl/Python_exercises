def mortgageCalcAdvanced():
    
    mortgage_amount = int(input("What's the mortgage amount? "))
    interest_rate = float(input("What's the interest rate? ")) / 100
    lenght_years = int(input("What's the lenght of the mortgage in years? "))
    
    
    def quarterlyPayment(mortgage, interest_rate, lenght_years):
        interest_rate = interest_rate / 4
        lenght_quarters = lenght_years * 4
        
        quarterly_payment = mortgage * ((interest_rate * ((1 + interest_rate)**lenght_quarters)) / (((1 + interest_rate)**lenght_quarters) - 1))
        return quarterly_payment
    
    def monthlyPayment(mortgage, interest_rate, lenght_years):
        lenght_months = lenght_years * 12
        interest_rate = interest_rate / 12
        
        monthly_payment = mortgage * ((interest_rate * ((1 + interest_rate)**lenght_months)) / (((1 + interest_rate)**lenght_months) - 1))
        return monthly_payment
    
    def weeklyPayment(mortgage, interest_rate, lenght_years):
        lenght_weeks = lenght_years * 52
        interest_rate = interest_rate / 52
        
        weekly_payment = mortgage * ((interest_rate * ((1 + interest_rate)**lenght_weeks)) / (((1 + interest_rate)**lenght_weeks) - 1))
        return weekly_payment
    
    def dailyPayment(mortgage, interest_rate, lenght_years):
        lenght_days = lenght_years * 365
        interest_rate = interest_rate / 365
        
        daily_payment = mortgage * ((interest_rate * ((1 + interest_rate)**lenght_days)) / (((1 + interest_rate)**lenght_days) - 1))
        return daily_payment
    
    compound_interval = int(input("What's the compound interval? \n1. Quarterly \n2. Monhly \n3. Weekly \n4. Daily\n"))
    if compound_interval == 1:
        print("Your quarterly payment will be {} dolars".format(round(quarterlyPayment(mortgage_amount,interest_rate,lenght_years),2)))
    elif compound_interval == 2:
        print("Your monthly payment will be {} dolars".format(round(monthlyPayment(mortgage_amount,interest_rate,lenght_years),2)))
    elif compound_interval == 3:
        print("Your weekly payment will be {} dolars".format(round(weeklyPayment(mortgage_amount,interest_rate,lenght_years),2)))
    elif compound_interval == 4:
        print("Your daily payment will be {} dolars".format(round(dailyPayment(mortgage_amount,interest_rate,lenght_years),2)))
