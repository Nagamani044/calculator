from calculator import add, subtract, multiply, divide

def run_calculator():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Add:", add(a, b))
    print("Subtract:", subtract(a, b))
    print("Multiply:", multiply(a, b))
    try:
        print("Divide:", divide(a, b))
    except ZeroDivisionError as e:
        print("Error:", e)
