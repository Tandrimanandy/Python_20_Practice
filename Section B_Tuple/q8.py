'''
Question 8: Student Registration Record
A college stores a student's roll number, name, course, and
semester in a tuple. Write a function that displays each field
separately and prints the complete student record.

'''

def student_record(record):
    roll_no, name, course, semester = record

    print(f"Roll number: {roll_no} \n Name: {name} \n Course: {course} \n Semester: {semester} \n Complete record: {record}")
student_record((101, "Tandrima Nandy", "MCA ", 4))
print()