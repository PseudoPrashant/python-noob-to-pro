# code to count the number of vowels in the given string

def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            count += 1
    return count

sentence = input("Enter a string: ")
print(f"The number of vowels are: {count_vowels(sentence)}")
