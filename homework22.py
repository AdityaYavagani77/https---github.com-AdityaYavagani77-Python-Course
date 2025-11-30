def square_it_out():
    start_range = int(input("Enter the beginning of the range: "))
    end_range = int(input("Enter the end of the range: "))
    
    square_values = []
    for num in range(start_range, end_range + 1):
        square = num ** 2
        square_values.append(square)
    
    odd_squares = []
    even_squares = []
    
    for value in square_values:
        if value % 2 == 0:
            even_squares.append(value)
        else:
            odd_squares.append(value)
            
    print("\nOdd Square Values:")
    print(odd_squares)
    
    print("\nEven Square Values:")
    print(even_squares)

square_it_out()