"""
import random

playing = True
number = str(random.randint(10,20))

print("I will generate a number from 10 to 20, and you have to guess the number one digit at a time ")

while playing:
    guess = input("Give me your best guess! \n")

    if number == guess:
        print("You win the game!")
        print(f"The number was {number}")
        break

    else:
        print("Your guess isn't quite right, please try agian! \n")
        
import random


user_choice = input("Choose rock, paper, or scissors: ").lower()

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)


print(f"\nYou chose: {user_choice}")
print(f"The computer chose: {computer_choice}\n")


if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'paper' and computer_choice == 'rock') or \
     (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("The computer wins!") 
    """

import math

print("The Floor and Ceiling  value of 23.56 :" + str(math.ceil(23.56)) +"," + str(math.floor(23.56 ))


