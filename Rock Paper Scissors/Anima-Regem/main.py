import random

option = ['Rock','Paper','Scissors']

def rock(cp):
    if (cp==1):
        print("Draw")
    elif(cp==2):
        print("Compuer Win")
    else:
        print("You Win")

def paper(cp):
    if(cp==1):
        print("You Win")
    elif(cp==2):
        print("Draw")
    else:
        print("Compuer Win")

def scissors(cp):
    if(cp==1):
        print("Compuer Win")
    elif(cp==2):
        print("You Win")
    else:
        print("Draw")


while True:
    print('\n\n')
    choice=input('''1 : Rock
2 : Paper
3 : Scissors
Any other to exit
    ''')
    cp = random.randint(1,3)
    
    if (choice =='1'):
        print(f"You chose {option[int(choice)-1]}")
        print(f"Computer chose {option[cp-1]}")
        rock(cp)
    elif (choice=='2'):
        print(f"You chose {option[int(choice)-1]}")
        print(f"Computer chose {option[cp-1]}")
        paper(cp)
    elif (choice=='3'):
        print(f"You chose {option[int(choice)-1]}")
        print(f"Computer chose {option[cp-1]}")
        scissors(cp)
    else:
        break
