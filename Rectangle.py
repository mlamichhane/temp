"""
    Program: To define the class for a Rectangle object
    Date   : April 2, 2024
    Author : Milan Lamichhane
"""

class Rectangle:
    def __init__(self, l, w):
        self.__length = l
        self.__width = w

    def get_perimeter(self):
        return (2 * (self.__length + self.__width))
    
    def get_area(self):
        return self.__length * self.__width
    
    def is_square(self):
        return (self.__length == self.__width)
    
    def get_width(self):
        return self.__width
    
    def get_length(self):
        return self.__length
    
    def set_width(self, w):
        self.__width = w

    def set_length(self, l):
        self.__length = l
        
    def __str__(self):
        return f"Rectangle with lenght {self.__length} and width {self.__width}."