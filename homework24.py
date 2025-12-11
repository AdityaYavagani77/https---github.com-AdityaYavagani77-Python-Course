test_dictionary = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print("--- Test Dictionary ---")
print(test_dictionary)
print("-----------------------")

user_input = input("Enter the value you want to check the frequency of (e.g., 1, 2, or 3): ")

try:
    target_value = int(user_input)
except ValueError:
    target_value = user_input
    print(f"Checking for value: '{target_value}' (as text)")

frequency = 0

for value in test_dictionary.values():
    if value == target_value:
        frequency += 1

print(f"\nThe frequency (number of occurrences) of the value '{target_value}' is: {frequency}")