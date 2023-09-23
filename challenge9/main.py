# Write a program that:
# • converts and outputs marks into
# grades
marks = int(input("Enter marks : "))

def grading(marks):
    if marks >= 75 and marks <= 100:
        grade = "A"
    elif marks >= 60 and marks < 75:
        grade = "B"
    elif marks >= 35 and marks < 60:
        grade = "C"
    elif marks < 35:
        grade = "D"
    else:
        grade = "-- Please enter valid marks --"

    return grade

print("Awarded grade : " + grading(marks))
