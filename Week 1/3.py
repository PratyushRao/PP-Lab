#Figure out the type of triangle from side lengths
a = float(input("Enter first side of the triangle: "))
b = float(input("Enter second side of the triangle: "))
c = float(input("Enter third side of the triangle: "))

if a==b==c:
    print("It is an equilateral triangle. ")

elif  a!=b and b!=c and c!=a:
    print("It is a scalene triangle")

else: 
    print("It is an isosceles triangle")