import random
import Logo

UserChoice = int(input("Enter 0 for Rock 1 for Paper and 2 for Seasers : "))
Computer_choice = random.randint(0,2)

print("\nComputer chooses :")
print(Logo.l[Computer_choice])
print("Your choice : ")
print(Logo.l[UserChoice])

if UserChoice == Computer_choice:
    print("Match is Draw")
if UserChoice == 0:
    if Computer_choice == 1:
        print("Computer wins")
    else:
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