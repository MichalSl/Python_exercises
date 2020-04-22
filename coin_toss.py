import random

def coinToss():
    number = int(input("How many coin tosses? "))
    
    heads = 0
    tails = 0
    toss = 0
    
    for x in range(number):
        toss = random.randint(0,1)
        
        if toss == 0:
            heads += 1
        else:
            tails += 1
            
    print("Heads: {}".format(heads))
    print("Tails: {}".format(tails))
