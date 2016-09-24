import random
rollagain=input("would you like to roll the dice again? Y/N: ")
while rollagain.upper() == "Y":
    print (random.randint(1,6))
    print (random.randint(1,6))
    rollagain=input("would you like to roll the dice again? Y/N: ")
else:
    print("done")
