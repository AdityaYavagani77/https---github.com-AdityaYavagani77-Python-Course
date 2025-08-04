"""
num_1 = int(input("Please enter a number:"))
num_2 = int(input("Please enter a number:"))
num_3 = int(input("Please enter any number:"))

if num_1 and num_2 and num_3:
    print("All the numbers are True")
else:
    print("At least one of the numbers is False")

if num_3 < 6 or num_2 < 6 or num_1 < 6:
    print("At least one of he numbers is less than 5 or 5")
else:
    print("The numbers are equal to or greater than 6")
"""
num_1 = int(input("Please enter a number:"))
num_2 = int(input("Please enter a number:"))

if not (num_1==num_2):
    print("These 2 numbers are not equal")
else:
    print("The numbers are equal")
