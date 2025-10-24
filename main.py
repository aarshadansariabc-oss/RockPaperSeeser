import random
import Logo
def lo(Computer_choice,UserChoice):
    print("Your choice : ")
    print(Logo.l[UserChoice])
    print("\nComputer chooses :")
    print(Logo.l[Computer_choice])

def whoWis(UserChoice, Computer_choice):
    if UserChoice == Computer_choice:
        print("Match is Draw")
    elif (UserChoice == 0 and Computer_choice == 2) or \
         (UserChoice == 1 and Computer_choice == 0) or \
         (UserChoice == 2 and Computer_choice == 1) :     
        print("You Win!")
    else:
        print("Computer Wins")
         

while True:
    UserChoice = int(input("Enter 0 Rock 1 Paper 2 Scisser : "))

    if UserChoice < 0 and UserChoice > 2:
        print("Invalid Input")
        break

    Computer_choice = random.randint(0,2)
    lo(Computer_choice,UserChoice)
    whoWis(Computer_choice,UserChoice)

    play_Again = input("Do You Want to play again 'Y' or 'N' : ").lower()

    if play_Again != 'y':
        print("Good Bye Have a Good Day")
        break


       

