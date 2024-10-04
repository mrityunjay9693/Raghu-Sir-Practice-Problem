"""
Problem 4
Problem: Write a Java program to read a side(length) of a square print the area and perimeter. 

Input Format: Enter a side(length): side (any number) 
Output Format:Area of square: area (any number, area of square)
              Perimeter of square: perimeter (any number, perimeter of square)
Sample Input: Enter side: 12 (any number)

Sample Output: Area of square: 144
               Perimeter of square: 48
Area of square: side * side
Perimeter of square: 4 * side 
"""

side = int(input("Enter side of square: "))
print("Area of square:", (side * side))
print("Perimeter of square:", (4 * side))
