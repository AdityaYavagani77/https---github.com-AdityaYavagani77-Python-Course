"""
num = int(input("Please enter a number:"))

for i in range(num):
    for j in range(i+1):
        print(  , end ="")
    print()
"""
num = int(input("Please enter a number:"))

extravar = 1

for i in range(num):
    for j in range(i+1):
        print(  extravar," " , end ="")
        extravar = extravar + 1
    print()
    