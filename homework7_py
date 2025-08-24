'''
#This is for converting  CHAR --> ASCII
user_input = input("Please enter a single letter or number: ")

if len(user_input) == 1:
    ascii_value = ord(user_input)
    print(f"The ASCII value of '{user_input}' is {ascii_value}")
else:
    print("Error: You must enter only one character.")

##################################################
'''




#This is for converting ASCII --> CHAR
user_input = (input("Please enter a ASCII value: "))
if user_input.isdigit():
    ascii_value = int(user_input)
   
    if 0 <= ascii_value <= 127:
        my_char = chr(ascii_value)
        print(f"The character for the ASCII value {ascii_value} is '{my_char}'")
    else:
        print("Error: The number is outside the standard ASCII range (0-127).")
else:
    print("Error: Invalid input. Please enter a number.")