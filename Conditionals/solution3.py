# Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

Student_Marks = int(input("What is your marks:"))

if Student_Marks >= 101:
    print("Please give a no. below or same as 100 ")
    exit()

if Student_Marks >= 90:
    grade = "A"
elif Student_Marks >= 80:
    grade = "B"
elif Student_Marks >= 70:
    grade = "C"
elif Student_Marks >= 60:
    grade = "D"
else:
    grade = "F"            

print(grade)    