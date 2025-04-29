"""
    Program: To calculate BMI of a person
    Date   : April 9, 2023
    Author : Milan Lamichhane
"""

from Rectangle import Rectangle

class AdvanceRectangle(Rectangle):
    def __init__(self, len, wdt, col):
        super().__init__(len, wdt)
        self.__color = col

    def set_color(self, col):
        self.__color = col

    def get_color(self):
        return self.__color
    
    def __str__(self):
        return f"Advanced Rectangle with length {super().get_length()}, width {super().get_width()} and color {self.__color}."
