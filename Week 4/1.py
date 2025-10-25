#Read 4 numbers and print in ascending order

a = int (input("Enter the first number: "))
b = int (input("Enter the second number: "))
c = int (input("Enter the third number: "))
d = int (input("Enter the fourth number: "))

l=[a,b,c,d]
l.sort()
print("The numbers in ascending order is: ", end="")
for i in l:
    print(i, end=" ")


