print("""***********************
      Calculator
      
      Operations:

      1.Add

      2.Subtrack

      3.Multiple

      4.Divide
      
***********************""")
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

operation = input("Enter the opearion number:")

if operation == "1":
    print("Result:", a + b)
elif operation == "2":
    print("Result:", a - b)
elif operation == "3":
    print("Result:", a * b)
elif operation == "4":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation number.")