try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(f"Sum = {a+b}\nDifference = {a-b}\nProduct = {a*b}")
    if b != 0:
        print(f"Quotient = {a//b}")
    else:
        print("Division by zero is not allowed.")
except ValueError:
    print("Please enter valid integers.")
