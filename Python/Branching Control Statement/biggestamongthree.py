"""
Problem 10:
Write a python program to read three integer value from user and print biggest among those three integer values.  
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2:
    if num1 > num3:
        print(num1, "is biggest number.")
    else:
        print(num3, "is biggest number.")
elif num2 > num3:
    print(num2, "is biggest number")
else:
    print(num3, "is the biggest number")
