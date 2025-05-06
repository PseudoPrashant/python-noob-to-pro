# function to check a word is palindrome or not 

def is_palindrome(text):
    if text==text[::-1]:
        return True
    else:
        return False
    
text = input("Enter a word to check palindrome : ").lower()
if is_palindrome(text):
    print(f"The word '{text}' is a palindrome")
else:
    print(f"The word '{text}' is not a palindrome")