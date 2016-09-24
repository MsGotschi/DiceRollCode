while True:
    import random
    print ("This is a dice rolling program")
    print ("Press the enter key to roll the dice")
    input ()
    number=random.randint(1,6)
    if number == 1:
        print ("[------------]")
        print ("[            ]")
        print ("[     ()     ]")
        print ("[            ]")
        print ("[------------]")
    if number == 2:
        print ("[------------]")
        print ("[            ]")
        print ("[   ()  ()   ]")
        print ("[            ]")
        print ("[------------]")
    if number == 3:
        print ("[------------]")
        print ("[   ()  ()   ]")
        print ("[            ]")
        print ("[     ()     ]")
        print ("[------------]")
    if number == 4:
        print ("[------------]")
        print ("[   ()  ()   ]")
        print ("[            ]")
        print ("[   ()  ()   ]")
        print ("[------------]")
    if number == 5:
        print ("[------------]")
        print ("[   ()  ()   ]")
        print ("[     ()     ]")
        print ("[   ()  ()   ]")
        print ("[------------]")
    if number == 6:
        print ("[------------]")
        print ("[   ()  ()   ]")
        print ("[   ()  ()   ]")
        print ("[   ()  ()   ]")
        print ("[------------]")
