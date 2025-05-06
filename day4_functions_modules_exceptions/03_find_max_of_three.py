# Code to find maximum among three numbers

def maximum(a, b):
    """Function to return maximum of two numbers."""
    if a >= b:
        return a
    else:
        return b

try:
    numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
    
    current_max = numbers[0]
    for num in numbers[1:]:
        current_max = maximum(current_max, num)
    
    print(f"The maximum among the given numbers is {current_max}")

except ValueError:
    print("Please enter valid numbers separated by spaces.")
except IndexError:
    print("Please enter at least two numbers.")
