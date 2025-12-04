def calculate_tuple_product(input_tuple):
  product = 1
  for number in input_tuple:
    product *= number
  return product

tup1 = (4, 3, 2, 2, -1, 18)
product1 = calculate_tuple_product(tup1)

print(f"Tuple 1: {tup1}")
print(f"Product of Tuple 1: {product1}")

print("-" * 30)

tup2 = (2, 4, 8, 8, 3, 2, 9)
product2 = calculate_tuple_product(tup2)

print(f"Tuple 2: {tup2}")
print(f"Product of Tuple 2: {product2}")