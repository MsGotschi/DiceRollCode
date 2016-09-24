#Chayann Bradford
#20/09/2016
#Task1: Dice Roll

import random
import sys

count=0
print("Hello World!")
amount=int(input("How many times do you want to role the dice?"))
while count <amount:
    num=random.randint(1,6)
    print("Your number is", num)
    count+=1

input("Press enter to close.")
sys.exit()
