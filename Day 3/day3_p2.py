# Program to Calculate the Area of a Circle and Triangle:
# Write a program to calculate the area of a circle given its radius and a triangle given its base and height. For example:
# Input: Radius: 5, Base: 10, Height: 4
# Output:Area of Circle: 78.5
# Area of Triangle: 20

radius = float(input("Enter radius: "))
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

area_circle = 3.14 * radius * radius # Area calculations
area_triangle = 0.5 * base * height # Area of Triangle

print("Area of Circle:", area_circle)
print("Area of Triangle:", area_triangle)


# output:
# Enter radius: 4
# Enter base of triangle: 9
# Enter height of triangle: 5
# Area of Circle: 50.24
# Area of Triangle: 22.5