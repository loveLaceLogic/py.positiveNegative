# Program to decide if a number is positive, negative, or zero

# Get user input
try:
    number = int(input("Enter a number: "))  # Convert input to an integer
    if number < 0:
        print("Your number is negative.")
    elif number > 0:
        print("Your number is positive.")
    else:
        print("Your number is zero.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
