"""my code
codes to understand the concept of sets and dictonaries

# set part
cities = input("Enter the name of cities sperated by space( ) : ").lower().split()
cities = set(cities) # converting list into sets

# printing the set
print (f"the name of cities in the set are: {cities}")

# checking if teh name of city is present in the set
city = input ("enter the name if the city you want to check : ").lower()

if city in cities:
    print(f"{city} is present in the set.")
else:
    print(f"{city} is not present in the set.")

# dictionary part
nameAge =  dict() # defining dictionary
for i in range(3): # storing the values
    name_age = input("Enter a name and age sepearted by space( ): ").split()
    nameAge[name_age[0]]=int(name_age[1])

# printing the data from dictionary
print('The data stored are as follows')

for i in nameAge:
    print (f"{i} : {nameAge[i]}")

********************************************************************************************************************"""

# Codes to understand the concept of sets and dictionaries

# Set part
cities = input("Enter the names of cities separated by space: ").lower().split()
cities = set(cities)

# Printing the set
print(f"\nThe names of cities in the set are: {cities}")

# Checking if the name of city is present in the set
city = input("\nEnter the name of the city you want to check: ").lower()
if city in cities:
    print(f"{city} is present in the set.")
else:
    print(f"{city} is not present in the set.")

# Dictionary part
nameAge = dict()

print("\nNow, enter 3 name-age pairs:")

for i in range(3):
    name_age = input(f"Enter name and age separated by space ({i+1}/3): ").split()
    nameAge[name_age[0]] = int(name_age[1])

# Printing the data from dictionary
print("\nThe data stored are as follows:")
for name, age in nameAge.items():
    print(f"{name} : {age}")
