"""
Day 3: Functions in Python - Explanation File

This file explains how functions work in Python, with examples.
All examples are written in a clear, block-style way for easier understanding.

Rules:
1. Functions group reusable code.
2. Functions can take inputs (parameters) and return outputs.
3. Keep functions short and focused on a single task.
4. Use descriptive names and docstrings.
"""

# --------------------------
# 1. Basic Function
# --------------------------

def greet(name):
    """
    Say hello to a person.
    
    Parameters:
    name: str - the name of the person
    
    Returns:
    None - just prints a message
    """
    print("Hello, " + name + "!")

# Example usage:
# greet("Alice")

# --------------------------
# 2. Function with Return Value
# --------------------------

def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Parameters:
    a: first number
    b: second number
    
    Returns:
    sum of a and b
    """
    result = a + b
    return result

# Example usage:
# total = add_numbers(5, 7)
# print(total)

# --------------------------
# 3. Function with Default Parameters
# --------------------------

def power(base, exponent=2):
    """
    Calculate the power of a number.
    
    Parameters:
    base: the number to raise
    exponent: the power (default is 2)
    
    Returns:
    base raised to the exponent
    """
    result = 1
    for i in range(exponent):
        result = result * base
    return result

# Example usage:
# print(power(5))      # 5^2
# print(power(2, 3))   # 2^3

# --------------------------
# 4. Function with Multiple Parameters
# --------------------------

def introduce(name, age, country):
    """
    Print a small introduction about a person.
    
    Parameters:
    name: person's name
    age: person's age
    country: person's country
    
    Returns:
    None
    """
    print("My name is " + name + ".")
    print("I am " + str(age) + " years old.")
    print("I live in " + country + ".")

# Example usage:
# introduce("Bilal", 24, "Turkey")

# --------------------------
# 5. Function Calling Another Function
# --------------------------

def square(number):
    """
    Return the square of a number.
    """
    return number * number

def sum_of_squares(a, b):
    """
    Return the sum of squares of two numbers by calling the square function.
    """
    square_a = square(a)
    square_b = square(b)
    result = square_a + square_b
    return result

# Example usage:
# print(sum_of_squares(3, 4))  # 3^2 + 4^2 = 25

# --------------------------
# 6. Main Block
# --------------------------

if __name__ == "__main__":
    
    print("1. Basic Function Example:")
    greet("Alice")
    print("\n")
    
    print("2. Function with Return Example:")
    total = add_numbers(5, 7)
    print("5 + 7 =", total)
    print("\n")
    
    print("3. Function with Default Parameter Example:")
    print("5^2 =", power(5))
    print("2^3 =", power(2, 3))
    print("\n")
    
    print("4. Function with Multiple Parameters Example:")
    introduce("Bilal", 24, "Turkey")
    print("\n")
    
    print("5. Function Calling Another Function Example:")
    print("Sum of squares of 3 and 4:", sum_of_squares(3, 4))