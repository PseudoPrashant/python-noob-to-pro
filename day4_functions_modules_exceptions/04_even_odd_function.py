# code to create a function which returns even or odd

def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

try:
    num = int(input("Enter a number: "))
    print(f"The number is {is_even(num)}")

except ValueError:
    print("Please enter a valid integer.")
