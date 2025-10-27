"""
var = 10

while var > 0:
    var= var-1
    if var ==5:
        continue
    print(f"n/Current variable value: {var}.")
print("Goodbye.")
"""
a = input("Please enter a word:")

for i in a:
    if (i == "A"):
        print("A is found")
        break
    else:
        print("A not found")