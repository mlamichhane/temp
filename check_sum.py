"""
    Program: To check the sum of two numbers
    Date   : April 9, 2023
    Author : Milan Lamichhane
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2

if result == 100:
    print("The result is 100")
else:
    if result > 100:
        print("The result exceeds 100")
    else:
        print("The result is less than 100")