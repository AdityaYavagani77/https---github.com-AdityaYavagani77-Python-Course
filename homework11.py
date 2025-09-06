number = int(input("Please enter a number: "))
power = int(input("Please enter the power of the number: "))
answer = 1
for count in range(1,power+1):
  answer = answer * number

print(f"The answer is {answer}")

