PI_VALUE = 3.14

def circle_circumference(r):
  circumference = 2 * PI_VALUE * r
  print(f"The circumference is: {circumference}")

radius_input = float(input("Enter the radius (r) of the circle: "))

print(f"You entered a radius of: {radius_input}")
circle_circumference(radius_input)