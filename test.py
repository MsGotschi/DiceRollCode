#Mohammed Shekh
#20/09/2016
#Task 1: Dice Roll

import random
import sys

count=0
Rollnum=1
print("Hello!")
amount=int(input("How many times do you want to role the dice? (Maximum of 4 times)"))
while count <amount:
    num=random.randint(1, 6)
    print("This is your ", Rollnum," Roll. Your number is ", num)
    count+=1
    Rollnum+=1
input("press Enter to close.")
sys.exit()