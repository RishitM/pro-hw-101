import random
def roll():
    no=random.randint(1,6)
    if no==1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif no==2:
        print("[-----]")
        print("[   0 ]")
        print("[     ]")
        print("[ 0   ]")
        print("[-----]")
    elif no==3:
        print("[-----]")
        print("[   0 ]")
        print("[  0  ]")
        print("[ 0   ]")
        print("[-----]")
    elif no==4:
        print("[-----]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[-----]")
    elif no==5:
        print("[-----]")
        print("[ 0 0 ]")
        print("[  0  ]")
        print("[ 0 0 ]")
        print("[-----]")
    elif no==6:
        print("[-----]")
        print("[ 0 0 ]")
        print("[ 0 0 ]")
        print("[ 0 0 ]")
        print("[-----]")
    else:
        print('')
response=input("Press y to roll dice and n to exit: ")
if response=="y":
    roll()
elif response=="n":
    print("Thanks for using")
else:
    print("Thanks for using")

