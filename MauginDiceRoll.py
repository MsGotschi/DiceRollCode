#
# Ryan Maugin
# 20/09/16
# Dice roll program which generates a random number between 1 and 6
#

import random

while True:
    again = int(input("Enter (1) to try again or (2) to end: "))

    if again != 1:
        print("Game ended!")
        break

    print("You rolled: {}".format(random.randint(1, 6)))



