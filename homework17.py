def shutdown(user_input):
    input_normalized = user_input.lower().strip()

    if input_normalized == "yes":
        return "Shutting down."

    elif input_normalized == "no":
        return "abort shut down"

    else:
        return "sorry."

print("--- Test 1: Yes ---")
print(shutdown("Yes"))

print("\n--- Test 2: no ---")
print(shutdown("no"))

print("\n--- Test 3: Invalid Input ---")
print(shutdown("Maybe"))