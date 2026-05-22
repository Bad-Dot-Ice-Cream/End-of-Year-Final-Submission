import os

#Clearing terminal functionality
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?:\n>  "))

    while should_accumulate:
        for symbol in operations:
            print(f"\n{symbol}")

        operation_symbol = input("\nPick an operation:\n>  ")
        num2 = float(input("What is the next number?:\n>  "))
        answer= operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:\n>  ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            clear()
            calculator()

calculator()