#Calculator 
from art import logo
#Addition 
def add(n1, n2): 
    return n1 + n2

#Subtraction
def subtract(n1, n2): 
    return n1 - n2

#Multiplication 
def multiply(n1, n2): 
    return n1 * n2 

#Division 
def divide(n1, n2): 
    return n1 / n2 

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#recursion 

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations: 
        print(symbol)
    should_continue = True 

    while should_continue:

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        #picking up the function
        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        decision = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'x' to escape: ")
        if decision == 'y':
            num1 = answer
        elif decision == 'n' :
            should_continue = False
            calculator()
        elif decision == 'x':
            should_continue = False
            exit()
calculator()
