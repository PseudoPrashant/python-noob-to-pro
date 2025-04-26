# Program: Calculate factorial of a number

try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        factorial = 1
        temp = num  # save original number for printing

        while num > 1:
            factorial *= num
            num -= 1

        print(f"The factorial of {temp} is {factorial}")

except ValueError:
    print("Please enter a valid integer value.")
