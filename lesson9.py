
q1 = str(input("Please enter your gender:"))
q2 = int(input("What is your age:"))
if q1 == "male":
    if q2 >= 18:
        print("You are male and are  18 or older")
    else:
        print("You are male and under 18")
else:
    print("You are female")