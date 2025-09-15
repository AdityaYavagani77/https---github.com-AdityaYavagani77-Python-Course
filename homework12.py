number = int(input("Pleae enter a 3-6 digit number"))
count = 0

if number == 0:
    count = 1  
else:
    number = abs(number)
    
    while number > 0:
        number = number // 10
        count += 1

print(f"The number of digits is: {count}")