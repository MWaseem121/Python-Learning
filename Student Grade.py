# =========================================================
# PROGRAM 1: Student Grade & Performance Evaluator
# =========================================================
print("=== Student Grade & Performance Evaluator ===")
studen_name = input("Enter student Name: ")
student_name = input("Enter Student Name: ")

try:
    math_score = float(inupt("Enter Match Score (0-100): "))
    science_score = float(inupt("Enter Science Score (0-100): "))
    english_score = float(inupt("Enter English Score (0-100): "))

    average_score = (math_score + science_score + english_score)
try:
    math_score = float(input("Enter Math score (0-100): "))
    science_score = float(input("Enter Science score (0-100): "))
    english_score = float(input("Enter English score (0-100): "))

    average_score = (math_score + science_score + english_score) / 3

    if average_score >= 90:
        grade = "A"
        feedback = "Excellent job! Keep it up."
    elif average_score >= 80:
        grade = "B"
        feedback = "Good job! Well done."
    elif average_score >= 70:
        grade = "C"
        feedback = "Satisfactory performance."
    elif average_score >= 60:
        grade = "D"
        feedback = "Needs improvement."
    else:
        grade = "F"
        feedback = "Failed. Hard work is required."

    print("\n" + "*"*45)
    print(f"            REPORT CARD: {student_name.upper()}")
    print("*"*45)
    print(f"Average Score: {average_score:.2f}%")
    print(f"Grade Assigned: {grade}")
    print(f"Teacher Remarks: {feedback}")
    print("*"*45)
except ValueError:
    print("Please enter valid numeric scores!")

print("\n")
