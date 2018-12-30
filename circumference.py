#Adrian Sharpless
#Last mod date: 12/26/2018

#This program calculates the area and circumference of a circle from its radius.
import math

radius_str = input("Enter the radius of your circle: ")
radius_int = int(radius_str)

circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

print("The circumference is:", circumference, \
      ", and the area is:",area)
