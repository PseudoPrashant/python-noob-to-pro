# Using function and recursion to find factorial of a number

def factorial(num):
    """Returns the factorial of a number using recursion."""
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

try:
    a = int(input("Enter a number: "))
    if a < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {a} is {factorial(a)}")
except ValueError:
    print("Please enter a valid integer value.")
