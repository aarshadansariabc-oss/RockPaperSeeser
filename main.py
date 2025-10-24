import random
import Logo
def lo():
    print("Your choice : ")
    print(Logo.l[UserChoice])
    print("\nComputer chooses :")
    print(Logo.l[Computer_choice])

def whoWis():
    if UserChoice == Computer_choice:
        print("Match is Draw")
    if UserChoice == 0:
        if Computer_choice == 1:
            print("Computer wins")
        elif Computer_choice == 2:
            print("You Wins")
    elif UserChoice == 1:
        if Computer_choice == 0:
            print("You Win")
        elif Computer_choice == 2:
            print("Computer wins")
    elif UserChoice == 2:
        if Computer_choice == 0:
            print("Computer wins")
        else:
            print("You wins")
    else:
        print("Invalid Input")

UserChoice = int(input("Enter 0 for Rock 1 for Paper and 2 for Seasers : "))
Computer_choice = random.randint(0,2)
if UserChoice >=  0 and UserChoice <=2:
    lo()
    isCheck = True
    while isCheck:
        whoWis()
        toRun = input("You Want to play again 'Y' Or 'N' : ").lower()
        if toRun == 'y':
            UserChoice = int(input("Enter 0 for Rock 1 for Paper and 2 for Seasers : "))
            Computer_choice = random.randint(0,2)
            lo()
            whoWis()
        else:
            isCheck =False
else:
    print("Invalid Input")


