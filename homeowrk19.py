while True:
    try:
        age = int(input("Please enter your age: "))
        
        print("\n Input successfully validated as an integer.")
        
        if age % 2 == 0:
            print(f"The entered age ({age}) is **Even**.")
        else:
            print(f"The entered age ({age}) is **Odd**.")
            
        break 

    except ValueError:
        print("\n VALUE ERROR: That is not a correct integer value for age.")
        print("Please enter a whole number without text or decimals.\n")

print("\n--- Program finished. Best of luck! ---")