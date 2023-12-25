# name = "Bob"
# age = 30
# print("Name: %s, Age: %d" % (name, age))

# name = "Charlie"
# age = 35
# print(f"Name: {name}, Age: {age}")

# print("One", "Two", "Three", sep="-")

# print("Hello", end="")
# print("Worlds")
# print("y")

# with open("output.txt", "w") as f:
#     print("This will be written to the file", file=f)
    

# print("Repeated", end="")
# print("Output", end="")
# print("Here")

# print("This is a tab\tTabbed Text")

# print("\u41A9")  # Prints Greek letter Omega

# num = 3.14159
# print("Formatted Number: {:.2f}".format(num))

# x = 10
# print("The value of x is:", x)  # Used for debugging

# my_tuple = ("apple", "banana", "cherry")
# print(",".join(my_tuple))

# item_list = ["Apple", "Banana", "Cherry"]
# for item in item_list:
#     print(f"{item: >10}")  # Right aligned with a width of 10
#     print(f"{item}")

# special_chars = "apple\n\tbanana"
# print(repr(special_chars))

# import sys

# sys.stdout = open("output.txt", "w")
# print("This goes to output.txt")
# sys.stdout = sys.__stdout__  # Reset stdout to default


# num = 42
# print(f"Binary: {bin(num)}, Octal: {oct(num)}, Hex: {hex(num)}")

# num = 1000000000
# print(f"Formatted Number: {num:,}")

# import sys

# print("An error occurred!", file=sys.stderr)

# print("\033[1;32;40m Bright Green Text \x1b[0m")
# 3 italic, 4 underline, 9 strikethrough



# \033[ or \x1b[ signals the start of an escape code sequence.
# 1;32;40 is a combination of formatting codes:
# 1: Makes the text bold.
# 32: Sets the text color to bright green.
# 40: Sets the background color to black.
# m terminates the sequence, indicating the end of the formatting commands.
# Bright Green Text is the text to be displayed.
# \x1b[0m or \033[0m resets the text formatting to default.
# 0: Resets all text formatting to default settings.



# class MyClass:
#     def __str__(self):
#         return "This is the string representation of MyClass"

#     def __repr__(self):
#         return "MyClass() instance"

# obj = MyClass()
# print(obj)  # Uses __str__
# print(repr(obj))  # Uses __repr__

# print("\U0001F600")  # Prints the 😀 emoji
# print("\u2713")  # Prints the checkmark symbol ✓





# from library import sum as s
# s.Sub(15,2)
# from library.sum import Sum,Sub
# Sum(5,5)
# Sub(10,5)
# print("Hello")
# from library.custom_print import printkar as print
# print("Hello")


# a=10
# result = eval("2 + 3 * 5")
# print(result)  # Output: 17

# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]

# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old")
# # Output:
# # Alice is 25 years old
# # Bob is 30 years old
# # Charlie is 35 years old

# colors = ['red', 'green', 'blue']

# for index, color in enumerate(colors):
#     print(f"{index + 1}: {color}")
# # Output:
# # Color 1: red
# # Color 2: green
# # Color 3: blue








