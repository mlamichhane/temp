"""
    Program: To use the Rectangle class to create objects
    Date   : April 2, 2024
    Author : Milan Lamichhane
"""


from Rectangle import Rectangle
from AdvanceRectangle import AdvanceRectangle

def main():

    box1 = Rectangle(3,4)
    box1._
    print("The perimeter of the rectangle is {:.2f}.".format(box1.get_perimeter()))
    print("The area of the rectangle is {:.2f}".format(box1.get_area()))
    print("Is the rectangle a square? {}.".format("Yes" if box1.is_square() else "No"))
    
    print("\n")

    length = float(input("Enter the lenght of the box: "))
    width = float(input("Enter the width of the box: "))

    box2 = Rectangle(length,width)

    print("The perimeter of the rectangle is {:.2f}.".format(box2.get_perimeter()))
    print("The area of the rectangle is {:.2f}".format(box2.get_area()))
    print("Is the rectangle a square? {}.".format("Yes" if box2.is_square() else "No"))

    print("\n")
    
    box3 = AdvanceRectangle(6,2,"red")
    print("The perimeter of advanced rectangle is {:.2f}.".format(box3.get_perimeter()))
    print("The area of advanced rectangle is {:.2f}".format(box3.get_area()))
    
    print(box3)

if __name__ == "__main__":
    main()