# program to understand the working of tuple and list simuntaneuosly

# inputing fruit list
fruits = input("enter the name of 5 fruits seperated by space: ").lower().split()

# inputing color list and converting it to tuple
colors = input("enter the name of 5 colors seperated by space: ").lower().split()
colors = tuple(colors)

# printing tuple and list
print(f"Fruits list: {fruits}")
print(f"Colors tuple: {colors}")

# combining both tuple and list
fruits.extend(colors)  # alternative to for loop

print(f"Combined list: {fruits}") 