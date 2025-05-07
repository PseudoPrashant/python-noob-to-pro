def check_anagram(str1, str2):
    # remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if sorted(str1) == sorted(str2):
        print(f"'{str1}' and '{str2}' are anagrams.")
    else:
        print(f"'{str1}' and '{str2}' are not anagrams.")

# input
str1 = input("Enter the first word or phrase: ")
str2 = input("Enter the second word or phrase: ")

check_anagram(str1, str2)
