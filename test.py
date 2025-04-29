import math

message = "Hello World"

for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print(" ")

def area_of_circle(radius):
    return math.pi * (radius ** 2)

print("{0:.2f}".format(area_of_circle(2)))