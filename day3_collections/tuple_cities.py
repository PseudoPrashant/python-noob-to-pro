# code to understand the use of tuples

cities = input("Enter the name of cities sperated by space( ) : ").lower().split()
cities = tuple(cities)

# printing the first city name
print(f"the name of the first city is {cities[0]}")

# printing the last city name
print(f"the name of the last city is {cities[-1]}")

# printing the number of cities in the tuple
print(f"the number of cities in the tuple are {len(cities)}")

# checking if teh name of city is present in the tuple
city = input ("enter the name if the city you want to check : ").lower()
index = 0
ispresent = False
for i in cities:
    if i == city:
        print(f"The city is present in the tuple at {index}")
        ispresent = True
    index+=1

if ispresent == False:
    print("city is not present in the tuple")