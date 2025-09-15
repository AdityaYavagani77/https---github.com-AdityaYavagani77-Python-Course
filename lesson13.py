user_input = input("Please enter a a word:")

charectar = input("Please enter a letter:")

sum = 0
for i in user_input:
    if i == charectar:
        sum = sum+1
print(f"The total occarance of the letter {charectar} in {user_input} is {sum}")

    