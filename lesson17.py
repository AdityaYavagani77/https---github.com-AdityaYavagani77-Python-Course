"""
due_amount = int(input("Please enter the amount that you are supposed to pay:"))
tip_amount = int(input("Also, please enter the percentage you want to tip:"))

def tip_calculator(total,percentage):
    return(total*percentage)/100

tip = tip_calculator(due_amount,tip_amount)
print(f"Your total tip is {tip}")
print(f"Your total expenditure is {tip + due_amount}")
"""
def cube(number):
    return(number*number*number)

def check_system(number):
    if (number%3 == 0):
        return cube(number)
    else:
        return "That the number is not divisible by 3 so I did not calculate the cube!"


real_number = int(input("Please enter a number to be cubed:"))

print(check_system(real_number))
