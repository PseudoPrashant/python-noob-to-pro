# code to understand def command and to add two numbers using functions

def add (a,b): #  defining the add function
    return a+b # retuning the sum 

# inputing the numbers
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The sum of {num1} and {num2} is {add(num1, num2)}")

except ValueError:
    print("Enter a integral value")