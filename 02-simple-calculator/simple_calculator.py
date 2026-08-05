# A simple calculator for the four basic operations, with divide-by-zero handling.

def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Operator must be one of + - * /")


def main():
    a = float(input("First number: "))
    op = input("Operator (+ - * /): ").strip()
    b = float(input("Second number: "))
    try:
        print(f"{a} {op} {b} = {calculate(a, op, b)}")
    except ZeroDivisionError as e:
        print(e)


if __name__ == "__main__":
    main()
