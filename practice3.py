import random


userr_choice = input("Choose rock, paper, or scissors: ").lower()

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)


print(f"\nYou chose: {userr_choice}")
print(f"The computer chose: {computer_choice}\n")


if userr_choice == computer_choice:
    print("It's a tie!")
elif (userr_choice == 'rock' and computer_choice == 'scissors') or \
     (userr_choice == 'paper' and computer_choice == 'rock') or \
     (userr_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("The computer wins!") 