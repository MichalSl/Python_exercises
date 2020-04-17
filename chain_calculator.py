def coins_counter():
    
    product = float(input("How much did the product cost? "))
    note = int(input("How much did you pay? "))
    
    amount = round((note - product) * 100)
    
    half_dolar = 50
    quarter = 25
    dime = 10
    nickel = 5
    cent = 1
    
    half_dolar_counter = 0
    quarter_counter = 0
    dime_counter = 0
    nickel_counter = 0
    cent_counter = 0
    total_coin_count = 0
    
    while amount != 0:
        if amount >= half_dolar:
            amount = amount - half_dolar
            half_dolar_counter += 1
            total_coin_count += 1

        elif amount >= quarter:
            amount -= quarter
            quarter_counter += 1
            total_coin_count += 1

        elif amount >= dime:
            amount -= dime
            dime_counter += 1
            total_coin_count += 1

        elif amount >= nickel:
            amount -= nickel
            nickel_counter += 1
            total_coin_count += 1

        elif amount >= cent :
            amount -= cent
            cent_counter += 1
            total_coin_count += 1
    
    print("You should receive {} coins: {} half dolars, {} quarters, {} dimes, {} nickels and {} cents.".format(total_coin_count,half_dolar_counter,quarter_counter,dime_counter,nickel_counter,cent_counter))
    
