"""
Problem: Write a Java program to read length and breadth of a reactangle from the user and print area and perimeter 
of the reactangle
Input Format: Enter length: length (any number)
              Enter breadth: breadth (any number) 
Output Format:Area of reactangle: area (any number, area of circle)
              Perimeter of reactangle: perimeter (any number, circumference of circle)
Sample Input: Enter length: 5 (any number)
              Enter breadth: 7 (any number)
 
Sample Output: Area of reactangle: 35
               Perimeter of reactangle: 24
Area of reactangle: length * breadth
Perimeter of reactangle: 2 * (length * breadth)
"""

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
print("Area of reactangle: ", (length * breadth))
print("Perimeter of reactangle: ", 2 * (length + breadth))
