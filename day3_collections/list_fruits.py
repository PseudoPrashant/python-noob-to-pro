# to store multiple fruit names in list and do operations on it

fruit= input("Enter the names of multiple fruits: ").split()
print(fruit)
print()

# first and last item in the list
print(f"first items is {fruit[0]} and the last item is {fruit[-1]}")
print()

# number of total itmes in list
print("the number of total iems in the list currently is ",len(fruit))
print()

# to add fruit in list
name = input("Enter a fruit name = ")
fruit.append(name)
print ("new list : ", fruit)
print()

# to remove fruit in list
name = input("Enter a fruit name already in the list= ")
fruit.remove(name)
print ("new list : ", fruit)
print()

# iterating through the list
print("Items in the list: ")
for i in fruit:
    print(i)