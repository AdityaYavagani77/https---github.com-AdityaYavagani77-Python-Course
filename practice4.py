import time

def coin_flip_game():

    print("Welcome to the Coin Flip Game!")
    
    while True:
        user_guess = input("Heads or Tails? (h/t): ").lower()
        if user_guess in ['h', 't']:
            break
        else:
            print("Invalid input. Please enter 'h' for Heads or 't' for Tails.")
            
    
    print("\nFlipping the coin...")
    time.sleep(1) 
    
    import random
    flip = random.randint(0, 1)
    
    if flip == 0:
        result = 'h'
        result_name = 'Heads'
    else:
        result = 't'
        result_name = 'Tails'

    print(f"It's {result_name}!")
    
    if user_guess == result:
        print("Congratulations! You guessed correctly!")
    else:
        print("Sorry, better luck next time!")

if __name__ == "__main__":
    coin_flip_game()