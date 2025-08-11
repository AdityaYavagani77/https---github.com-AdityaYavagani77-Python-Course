"""
a = ["milk", "eggs", "bread",]
b = ["milk", "eggs", "bread"]
c = a

print(a is c)
print(a is b)
print(a is not c)
print(a is not b)

a = 5 #0101
b = 3 #0011

print(a&b)
print(a|b)
print(a^b)
print(a<<b)
print(a>>b)
"""
print("Enter your the marks you got on your tests out of 100")

mark_1 = int(input("English:"))
mark_2 = int(input("Science:"))
mark_3 = int(input("Math:"))
mark_4 = int(input("Geography:"))
mark_5 = int(input("P.E:"))

avg = (mark_1+mark_2+mark_3+mark_4+mark_5)/5

if avg >= 91:
   print("A+")

elif avg >= 81:
   print("A")
elif avg >= 71:
   print("B")
elif avg >= 61:
   print("C")
elif avg >= 51:
   print("D")
else:
   print("F")