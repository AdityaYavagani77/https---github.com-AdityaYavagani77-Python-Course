"""
num = int(input("Please enter a positive or negtive number:"))

if num > 0:
   print("Your number is postive")
else:
   print("Your number is negitive ")
"""
item = str(input("What item are you buying?"))
price = int(input("What is the cost of your item?"))
selling = int(input("What price are you selling it for?"))

if selling > price:
    print("You are making a profit!")
    print( "Your profit is",selling-price)
else:
    print("You are getting a loss of money?")
    print("Your loss is", price-selling)
