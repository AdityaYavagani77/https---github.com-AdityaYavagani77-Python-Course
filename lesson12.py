"""
User = int(input("Enter a number:"))
sum = 0

while User > 0:
    sum = sum+User
    User = User - 1
print(sum)

while True:
    print("Aditya")
"""
Input = int(input("Enter a 3 digit number:"))
orignal_num = Input

digit_1 = Input%10
Input = Input//10

digit_2 = Input%10
Input = Input//10

print(digit_1,digit_2,Input)

answer = (digit_1**3)+(digit_2**3)+(Input**3)

if answer == orignal_num:
    print("Your number is an armstrong number!!")
else:
    print("Your number is no an armstrong number.")


