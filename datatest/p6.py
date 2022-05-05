import random

random_number =  random.randint(-100,100)
if random_number < 0 :
    print ("Random integer: ",random_number)
    print ("The number is negative")
else:
    print ("Random integer: ", random_number)
    print ("The number is positive")
    print ("The square root of", random_number, "is", round((random_number**0.5), 4))
