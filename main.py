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
    elif UserChoice == 0 and Computer_choice ==1:
        print("Computer Wins")
    elif UserChoice == 1 and Computer_choice == 2:
        print("Computer Wins")
    elif UserChoice == 2 and Computer_choice == 0:
        print("Computer Wins")
    else:
        print("You Win !")
         
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
        else:
            isCheck =False
else:
    print("Invalid Input")


