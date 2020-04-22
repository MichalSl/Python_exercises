def tempConverter():

    while True:
        try:
            unit = int(input("Press:\n1. To convert to Fahrennheit\n2. To convert to Celsius\n"))
        except ValueError:
            print("Enter 1 or 2")
            print("\n")
        else:
            if unit == 1:
                temperature = int(input("\nEnter the temperature: "))
                temperature_convert = round((temperature / 5) * 9 + 32,2)
                print("{} degrees Celsius equals {} degrees Fahrenheit".format(temperature,temperature_convert))
                break

            elif unit == 2:
                temperature = int(input("Enter the temperature: "))
                temperature_convert = round((temperature -32) / 9 * 5)
                print("{} degrees Fahrenheit equals {} degrees Celsius".format(temperature,temperature_convert))
                break

            else:
                print("Enter 1 or 2")
                continue

def speedConverter():
    while True:
        try:
            unit = int(input("Press:\n1. To convert to mph\n2. To convert to Km\h\n"))
        except ValueError:
            print("Enter 1 or 2")
            print("\n")
        else:
            if unit == 1:
                speed = int(input("\nEnter the speed: "))
                speed_conv = round(speed * 0.62,2)
                print("{} km\h equals {} mph".format(speed,speed_conv))
                break

            elif unit == 2:
                speed = int(input("Enter the speed: "))
                speed_conv = round(speed * 1.6,2)
                print("{} mph equals {} km\h".format(speed,speed_conv))
                break

            else:
                print("Enter 1 or 2")
                continue

def Converter():
    
    print("Welcome to the converter!")
    
    while True:
        try:
            conversion = int(input("Press:\n1. To convert temperature\n2.To convert speed\n"))
        except ValueError:
            print("Enter 1 or 2")
            print("\n")
        else:
            if conversion == 1:
                tempConverter()
            elif conversion == 2:
                speedConverter()
            else:
                print("Enter 1 or 2!")
                continue
        
        reply = input("Do you want to try again? Y / N ")
        
        if reply.lower().startswith("y"):
            continue
        else:
            print("Bye")
            break
