from collections import namedtuple

if __name__ == "__main__":
    # Gets the number of students and the fields
    student_number = int(input())
    student = namedtuple('student', input())
    # Intializing a variable to hold the total marks
    total_marks = 0
    for i in range(student_number):
        # Mahing named tuple for every student and updating the total marks variable
        student_i = student(*input().split())
        total_marks += int(student_i.MARKS)
    # Printing the average marks corrected to 2 decimal places.
    print("%.2f" %(total_marks/student_number))