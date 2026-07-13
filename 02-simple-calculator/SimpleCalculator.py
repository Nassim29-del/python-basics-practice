"""
Simple Calculator
Performs basic arithmetic on two numbers, with division-by-zero handling.
"""


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a * b."""
    return a * b


def divide(a, b):
    """Return a / b, or None if dividing by zero."""
    if b == 0:
        return None
    return a / b


def main():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    # Read both numbers, guarding against non-numeric input
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    op = input("Enter the operation (+ - * /): ")

    if op == "+":
        print(f"{a} + {b} = {add(a, b)}")
    elif op == "-":
        print(f"{a} - {b} = {subtract(a, b)}")
    elif op == "*":
        print(f"{a} * {b} = {multiply(a, b)}")
    elif op == "/":
        result = divide(a, b)
        if result is None:
            print("Error: cannot divide by zero.")
        else:
            print(f"{a} / {b} = {result}")
    else:
        print("Unknown operation.")


if __name__ == "__main__":
    main()