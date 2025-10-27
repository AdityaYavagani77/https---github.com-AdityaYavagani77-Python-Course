"""
var = 10

while var > 0:
    var= var-1
    if var ==5:
        continue
    print(f"n/Current variable value: {var}.")
print("Goodbye.")

a = input("Please enter a word:")

for i in a:
    if (i == "A"):
        print("A is found")
        break
    else:
        print("A not found")
        """

for x in range(21):
    if x % 20==0:
        print("twist")
    
    elif x % 15==0:
        pass
    
    elif x % 5==0:
        print("buzz")

    elif x % 3==0:
        print("fizz")

    else:print(x)