"""
Day 4: Modules in Python - Explanation File

This file explains Python modules, how to create and use them, with clear examples.
All examples are written in block style for better understanding.

Rules:
1. A module is a file containing Python code (functions, classes, variables).
2. Modules help organize code into separate files for reusability.
3. Use import statements to access modules in other files.
4. Avoid circular imports.
"""

# --------------------------
# 1. Using a Built-in Module
# --------------------------

# Example: math module
import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle using math.pi
    
    Parameters:
    radius: radius of the circle
    
    Returns:
    area of the circle
    """
    area = math.pi * radius * radius
    return area

# Example usage:
# print(calculate_circle_area(5))

# --------------------------
# 2. Creating Your Own Module
# --------------------------

# Suppose we create a file called my_utils.py with the following functions:
# my_utils.py
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
"""

# We can import and use it in another file

# import my_utils
# result = my_utils.add(5, 3)
# print(result)

# --------------------------
# 3. Import Specific Functions
# --------------------------

# from my_utils import add
# result = add(10, 7)
# print(result)

# --------------------------
# 4. Import with Alias
# --------------------------

# import my_utils as mu
# result = mu.subtract(15, 4)
# print(result)

# --------------------------
# 5. Using Python Standard Library Modules
# --------------------------

# Example: datetime module
import datetime

def current_date_time():
    """
    Return the current date and time
    """
    now = datetime.datetime.now()
    return now

# Example usage:
# print(current_date_time())

# --------------------------
# 6. Main Block
# --------------------------

if __name__ == "__main__":
    
    print("1. Circle area example:")
    area = calculate_circle_area(5)
    print("Area of circle with radius 5:", area)
    print("\n")
    
    print("2. Using a custom module (example code):")
    print("If my_utils.py exists, you can import add or subtract functions.")
    print("\n")
    
    print("3. Current date and time example:")
    now = current_date_time()
    print("Current date and time:", now)