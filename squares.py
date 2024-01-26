valid_input = False

while not valid_input:
    user_input = input("Enter a number: ")

    if user_input.isdigit():
        user_input = float(user_input)
        result = user_input ** 2
        
        print(f"{result} is the exact result of {user_input} squared!")
        valid_input = True
    else:
        print("Input is not a number. Please enter a number.")