"""
Problem 6
Write a python program to read two integer values and perform all arithmetic operation.
Input Format: Enter first number: num1 (any number)
              Enter first number: num2 (any number)
Output Format: Addition: t1 (addition result)
               Substraction: t2 (substraction result)
               Product: t3 (product result)
               Division: t4 (division result)
Sample Input: Enter side: 4
                          7
Sample Output: Addition: 6 
               Substraction: 2
               Product: 8
               Division: 2
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Addition: ",(num1+num2))
print("Substraction:",(num1-num2))
print("Product: ",(num1*num2))
print("Division: ",(num1/num2))
