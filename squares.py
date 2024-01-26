valid_input = False

while not valid_input:
    user_input = input("Enter a number: ")

    if user_input.isdigit():
        user_input = float(user_input)
        result = user_input ** 2
        
        print(f"The square of {user_input} is: {result}")
        valid_input = True
    else:
        print("Invalid input. Please enter a numerical value.")