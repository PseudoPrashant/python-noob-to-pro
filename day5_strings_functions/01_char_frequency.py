# Program to count the frequency of each character in a string

def char_frequency(text):
    freq = dict()
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Taking input from user
text = input("Enter a string: ")

# Calling the function
frequency = char_frequency(text)

# Displaying the frequency
print("Character Frequency:")
for char, count in frequency.items():
    print(f"{char} : {count}")
