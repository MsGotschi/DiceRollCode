import random

def roll (sides=6):
    numberrolled = random.randint (1,sides)
    return numberrolled

def main():
    faces = 6
    rolling = true
    while rolling:
        rolldiceagain = input('roll dice again? ENTER = roll. Q=Quit?')
        if rolldiceagain.lower() != 'q':
            numberrolled = roll(faces)
            print('you rolled a', numberrolled)
            else:
                rolling = false
                print('goodbye')




