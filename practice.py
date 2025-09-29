user_enter = input("Please enter a number or character:")

try:
    int(user_enter)
    print("This is a number!")
except ValueError:
    print("This is a character!")                   
