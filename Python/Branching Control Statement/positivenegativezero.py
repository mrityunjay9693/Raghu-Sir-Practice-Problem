"""
Problem 7:
Write a python program to print user enter number is positive or negative or zero.
"""
number = int(input("Enter a number: "))
if  number == 0:
    print("Zero.")
elif number > 0:
    print("Positive.")
else:
    print("Negative.")