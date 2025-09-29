number_str = input("Enter decimal number: ")

if '.' in number_str:
    integer_part, fractional_part = number_str.split('.')
    integer = int(integer_part)
    fraction = float("0." + fractional_part)
else:
    integer = int(number_str)
    fraction = 0.0

binary_int = ""
temp_num = integer
if integer == 0:
    binary_int = "0"
while temp_num > 0:
    binary_int = str(temp_num % 2) + binary_int
    temp_num //= 2

binary_frac = ""
temp_frac = fraction
limit = 8

while temp_frac > 0 and len(binary_frac) < limit:
    temp_frac *= 2
    binary_frac += str(int(temp_frac))
    temp_frac -= int(temp_frac)

if fraction == 0.0:
    print("Binary:", binary_int)
else:
    print("Binary:", binary_int + "." + binary_frac)