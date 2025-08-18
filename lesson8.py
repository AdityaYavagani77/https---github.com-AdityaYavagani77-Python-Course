"""
a = 2
b = 6
h = 7

print(b+h**a)
"""

a = int(input("Please enter a number:"))
b = int(input("Please enter another number:"))

if a%b == 0:
    print("a is divisible by b")
else:
    print("a is not divisible by b")

if b%a == 0:
    print("b is divisible by a")
else:
    print("b is not divisible by a")