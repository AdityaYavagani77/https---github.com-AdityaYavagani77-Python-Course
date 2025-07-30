print("Finally, I can take my jacket off.") 
print("But can you inform me what to where according to the tempreture")
print("Ok Rohan")

user_input = int(input("Tell me the temprature!"))

if user_input > 40:
    print("According to the temprature, must wear a shorts with a white short sleeve. it's too hot!!")
if user_input > 30:
    print("It is cooler then expected, please were pants with a shirt of your choice")
if user_input > 20:
    print("Wear hat ever you want, It's the perfect temprature.")
if user_input > 10:
    print("It is very cold, please wear a pant with a soft long sleeved shirt.")
else:
    print("It is too cold!!!!!! you still have to wear your jacket and pullover")

print("Thank you for asking me Rohan")