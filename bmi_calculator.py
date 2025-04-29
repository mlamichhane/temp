"""
    Program: To calculate BMI of a person
    Date   : April 9, 2023
    Author : Milan Lamichhane
"""

name = input("What is your name? ")
weight = float(input("What is your weight in kilo? "))
height = float(input("What is your height in meters? "))

bmi = weight/(height ** 2)

print("\n{0}'s BMI is {1:.2f}".format(name, bmi))
 
if bmi < 18.5:
    print("{0} is underweight".format(name))
elif bmi >= 18.5 and bmi <=24.9:
    print("{0} is healthy".format(name))
elif bmi >= 25 and bmi <=29.9:
    print("{0} is overweight".format(name))
else:
    print("{0} is obese".format(name))
