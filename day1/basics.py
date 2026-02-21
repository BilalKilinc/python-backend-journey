# swapping values

a = 3
b = 4
a, b = b, a

print(a, b)

###############

i = 1
i += 1  # i = i + 1
print(i)

###############

a = "python programming language"

print(a[2:20:2])  # prints from index 2 to 20 by stepping 2 characters at a time

# a[0] = "P"  strings are immutable, so this would raise an error

print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep="---")  # the sep parameter lets us define a custom separator

# FORMATTING
name = "Ali"
age = 25

print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

a = 10
b = 20
print("The sum of {:.2f} and {:.2f} is {:.2f}".format(a, b, a + b))  # format numbers to 2 decimal places

x = int(input("Enter a number: "))  # without int(), input is treated as a string
print("Entered number =", x)