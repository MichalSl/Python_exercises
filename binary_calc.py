def binaryToDecimal():

    binary_number = input("Enter a binary number: ")
    
    binary_number_list = [int(x) for x in binary_number] # creating a list of binary digits of the binary number
    
    
    binary_number_list_reverse = binary_number_list[::-1] # reversing the list
    
    
    powers = [x for x in range(0,len(binary_number_list_reverse))] # creating a list of powers
    
    len_powers = len(powers)
    
    print(len(powers) - 1)
    
    counter = 0
    
    decimal_list = []
    
    while counter <= len(powers) - 1:
        for x in binary_number_list_reverse:
            decimal_list.append(x * (2 ** counter))
            counter += 1
    
    print("Number {} in binary is {}".format(binary_number,sum(decimal_list)))
