# code to get prime numbers using funtions

def is_prime(n):
    temp = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            temp=False
            break
    return temp



try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        raise ValueError("Input must be a positive integer.")
    if num >= 2:
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    else:
        print(f"{num} is not a prime number (only numbers greater than 1 can be prime).")


except ValueError:
    print("enter a value positive integer") 