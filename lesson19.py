
try:
    number = int(input("Enter a number:"))
    print(f"The number entered is {number}")

except ValueError as ex:
    print(f"Exeception: {ex}")
    