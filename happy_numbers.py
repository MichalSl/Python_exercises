def HappyNumbers():
    
    print("Welcome to the happy numbers checker!")
    
    while True:
        try:
            original_number = int(input("Enter a number: "))    # the number input
            
        except ValueError:
            print("Enter a number: ")
            
        else:
            number = original_number    # copy of the original number to operate with
            new_number = 0 
            counter = 0    # counter to count steps
            results = []    #list of results of the operations
    
            if number == 1:
                print("Number {} is a happy number".format(original_number))



            else:
                while counter < 20:    # setting counter to 20 tries
                    number_str = str(number)    # creating a string of the number
                    new_number_list = [int(x)**2 for x in number_str]    # creating a list of squared digits of the number
                    new_number = sum(new_number_list)    # sum of the squared digits

                    if new_number == 1:    # if the sum of squared digits (new_number) = 1 - original number is happy
                        print("Number {} is a happy number".format(original_number))
                        counter += 1
                        print(results)
                        
                        reply = input("Do you want to try again? Y / N ")
                    
                        if reply.lower().startswith("y"):
                            continue
                        else:
                            print("Bye!")
                            break

                    else:    # if the sum of squared digits (new_number) != 1 try again and increase the counter
                        counter += 1
                        results.append(new_number)
                        number = new_number
                        continue

                else:    # if after 20 tries the sum of the squared digits != 1 ---> the original number is not happy 
                    print("Number {} is not happy number".format(original_number))
                    
                    reply = input("Do you want to try again? Y / N ")
                    
                    if reply.lower().startswith("y"):
                        continue
                    else:
                        print("Bye!")
                        break
                    
                    
            
