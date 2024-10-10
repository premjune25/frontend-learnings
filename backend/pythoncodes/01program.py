# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    # Check for division by zero
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main calculator function
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Loop until the user chooses to exit
    while True:
        # Prompt user for operation choice
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if the choice is a valid operation
        if choice in ['1', '2', '3', '4']:
            # Prompt user for two numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the selected operation and display the result
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

        # Exit option
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break  # Exit the loop

        # Handle invalid input
        else:
            print("Invalid input. Please select a valid operation.")

# Entry point of the program
if __name__ == "__main__":
    calculator()
