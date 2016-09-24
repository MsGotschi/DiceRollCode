import random
max=6
min=1

roll="Yes"

while roll=="Yes" or roll=="Y":
    print("Rolling the dice...")
    print("The dice rolled the values: ")
    print (random.randint(min,max))
    print (random.randint(min,max))

    roll= input("Roll the dice again? ")