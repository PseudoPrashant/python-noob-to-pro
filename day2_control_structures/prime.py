# Program: Check if a number is prime or not

try:
    num = int(input("Enter a number: "))

    if num > 1:
        # Special case for 2
        if num == 2:
            print("2 is a prime number")
        else:
            for i in range(2, int(num**0.5) + 1):  # Faster check till square root of num
                if num % i == 0:
                    print(f"{num} is not a prime number")
                    break
            else:
                print(f"{num} is a prime number")

    elif num == 0 or num == 1:
        print(f"{num} is neither prime nor composite")
    else:
        print("Negative numbers are not prime")

except ValueError:
    print("Please enter a valid integer input.")
