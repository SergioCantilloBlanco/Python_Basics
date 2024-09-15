def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    operations = {
        "addition": add,
        "subtraction": subtract,
        "multiplication": multiply,
        "division": divide
    }

    print("What operation would you like to perform?")
    for operation in operations:
        print(operation.capitalize())

    while True:
        user_input = input("Operation: ").lower()
        
        if user_input in operations:
            first_number = get_number("First number: ")
            second_number = get_number("Second number: ")
            
            try:
                result = operations[user_input](first_number, second_number)
                print("Result:", result)
                break
            except ValueError as e:
                print(e)
                break
        else:
            print("Please enter a valid operation.")

if __name__ == "__main__":
    main()
