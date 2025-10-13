
due_amount = int(input("Please enter the amount that you are supposed to pay:"))
tip_amount = int(input("Also, please enter the percentage you want to tip:"))

def tip_calculator(total,percentage):
    return(total*percentage)/100

tip = tip_calculator(due_amount,tip_amount)
print(f"Your total tip is {tip}")
print(f"Your total expenditure is {tip + due_amount}")
