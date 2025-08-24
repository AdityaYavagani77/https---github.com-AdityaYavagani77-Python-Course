character = input("Please enter a singular letter or number: ")

alphanumeric_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

if character in alphanumeric_characters:
    print(f"The character '{character}' is a letter or a number.")
else:
    print(f"The character '{character}' is neither a letter nor a number.")