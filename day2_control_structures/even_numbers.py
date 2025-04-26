# Program: Print even numbers up to a given number

try:
    num = int(input("Enter a value: "))

    if num < 2:
        print("There are no even numbers in this range.")
    else:
        print("Even numbers are:", end=" ")
        for i in range(2, num+1, 2):
            print(i, end=" ")
        print()  # to move cursor to next line after printing all numbers

except ValueError:
    print("Please enter a valid integer value.")
