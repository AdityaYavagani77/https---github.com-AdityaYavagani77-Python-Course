"""
def sports():
    print("Cricket Rules!")
    print("Soccer Forever!")
    print("Basketball is the Best!")

sports()
sports()
sports()
sports()

def weather_functions():
    print("Summer is very very hot.")
    print("Winter is ver very cold.")
    print("Autumn is dry and mildly cold.")
    print("Spring is pleasent and has lots of flowers.")

weather_functions()
"""

def Addition(a,b):
    print(f"{a}+{b} = {a+b} ")

def Subtraction(a,b):
    print(f"{a}-{b} = {a-b} ")

def Multiplication(a,b):
    print(f"{a}*{b} = {a*b} ")

def Division(a,b):
    print(f"{a}/{b} = {a/b} ")

x = int(input("Please enter a number to be Divided, Multiplied, Subtracted and Added:"))
y = int(input("Please enter another number to be Divided, Multiplied, Subtracted and Added wit the other number:"))

Division(x,y)

Multiplication(x,y)

Subtraction(x,y)

Addition(x,y)