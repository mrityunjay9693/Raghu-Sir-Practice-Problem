"""
Problem 1
Write a java program to read name, mobile number, 10th percentage, 12th percentage, and degree percentage 
and print in followingformat:

Input Format: Enter Student's name: Mrityunjay Kumar.
              Enter Mobile Number: 80029452
              Enter 10th Percentage: 77.69
              Enter 12th percentage: 68.82
              Enter Graduation Degree Percentage: 73.82 

Output Format:Student's name: Mrityunjay Kumar.
              Mobile Number: 80029452
              10th Percentage: 77.69
              12th percentage: 68.82
              Graduation Degree Percentage: 73.82
"""

print("--------------------------------------------------")
print("                Student's Details                 ")
print("--------------------------------------------------")
student_name = input("Enter Student's name: ")
mobile_number = int(input("Enter Mobile Number: "))
tenth_percent = float(input("Enter 10th Percentage: "))
twelfth_percent = float(input("Enter 12th percentage: "))
graduation_percent = float(input("Enter Graduation Degree Percentage: "))
print("--------------------------------------------------")
print("                Student's Details                 ")
print("--------------------------------------------------")
print("Student's name: ", student_name)
print("Mobile Number: ", mobile_number)
print("10th Percentage: ", tenth_percent)
print("12th percentage: ", twelfth_percent)
print("Graduation Degree Percentage: ", graduation_percent)
