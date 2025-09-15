"""
user_input = input("Please enter a a word:")

charectar = input("Please enter a letter:")

sum = 0
for i in user_input:
    if i == charectar:
        sum = sum+1
print(f"The total occarance of the letter {charectar} in {user_input} is {sum}")
"""
upper = int(input("Please enter the upper limit:"))
lower = int(input("Please enter the lower limit:"))

for i in range(lower,upper):
    if i > 1:
        for anything in range(2, i):
            if i % anything == 0:

                break
            else:
                print(i)