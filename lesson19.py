"""
try:
    number = int(input("Enter a number:"))
    print(f"The number entered is {number}")

except ValueError as ex:
    print(f"Exeception: {ex}")
"""

try:
    num1,num2 = eval(input("Enter 2 numbers, each one seperated with a comma :"))

    result = num1 / num2
    print(f"The division of your numbers is {result}")

except ZeroDivisionError:
    print("Division by zero is not possible!!")

except SyntaxError:
    print("Comma is missing. Write the numbers seperated with a comma e.g 1 , 2 ")

except:
    print("Wrong input!!")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")