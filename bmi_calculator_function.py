"""
    Program: To calculate BMI of a person
    Date   : April 21, 2023
    Author : Milan Lamichhane
"""
 
import bmi

if __name__ == "__main__":
    name = input("What is your name? ")
    weight = float(input("What is your weight in kilo? "))
    height = float(input("What is your height in meters? "))

    bmi.calc_bmi(name, weight, height)
    #bmi.calc_bmi(50, 1.9)

    bmi.message()

