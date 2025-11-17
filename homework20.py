import math

def calculate_trig_values(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    print(f"--- Calculating Trig Values for {angle_degrees}° ---")
    print(f"Angle in radians: {angle_radians:.4f}")

    sine_value = math.sin(angle_radians)
    cosine_value = math.cos(angle_radians)

    if abs(math.cos(angle_radians)) < 1e-9:
        tangent_value = "Undefined"
    else:
        tangent_value = math.tan(angle_radians)

    print(f"Sine (sin):   {sine_value:.4f}")
    print(f"Cosine (cos): {cosine_value:.4f}")
    print(f"Tangent (tan): {tangent_value}")

try:
    user_input = input("Enter the angle in degrees to calculate trigonometric values: ")
    angle = float(user_input)
    calculate_trig_values(angle)

except ValueError:
    print("\nError: Invalid input. Please enter a numerical value for the angle.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")