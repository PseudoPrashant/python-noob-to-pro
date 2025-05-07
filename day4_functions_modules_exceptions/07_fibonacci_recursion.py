#code to leanrn about fibonacci using recursion
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 
    

# Test the function with a few examples
try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        raise ValueError("Input must be a positive integer.")
    print(f"The first {num} Fibonacci numbers are:")
    for i in range(1, num + 1):
        print(fibonacci(i), end=' ')


except ValueError as e:
    print(f"Error: {e}")