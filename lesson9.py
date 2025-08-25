"""
q1 = str(input("Please enter your gender:"))
q2 = int(input("What is your age:"))
if q1 == "male":
    if q2 >= 18:
        print("You are male and are  18 or older")
    else:
        print("You are male and under 18")
else:
    print("You are female")
"""
Medical_cause = input("Do you have a medical cause:")

if Medical_cause == "yes":
    print("You are allowed to appear!")

elif Medical_cause == "no":
    Attendance = float(input("Put in your attendance percentage:"))
    if Attendance >= 75:
        print("you are allowed to appear!")
    else:
        print("you are not allowed to appear")