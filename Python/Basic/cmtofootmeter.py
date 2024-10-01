"""
Problem: Write a python program to read a length of a pipe from the user in 'cm'and print the length in 'foot' and 'meter'.
print in followingformat:
Input Format: Enter length: n (any number) 
Output Format:length in foot: area (any number, area of square)
              length in meter: c (any number, perimeter of square)
Sample Input: Enter side: 12
Sample Output: Area of square: 144 
               Perimeter of square: 48
                     
You have to take input from user as length of pipe in cm and then convert it to foot and in meter and print it.
1 meter : 100 cm
1 foot : 30.48 sm
"""

length_in_cm = int(input("Enter length of pipe in cm: "))
print("Length of pipe in foot:", (length_in_cm / 30.48))
print("Length of pipe in meter:", (length_in_cm / 100))
