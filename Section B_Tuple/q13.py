'''
Question 13: Employee Attendance Record
A company stores an employee's ID, name, and attendance status
in a tuple. Write a function that displays the record and reports
whether the employee is present or absent.

'''

def attendance_record(record):
    emp_id, name, status = record

    print(f"Employee ID: {emp_id} \n Name: {name}")
    if status.lower() == "present":
        print("Status will be Present")
    else:
        print("Status will be Absent")

attendance_record(("241001271061", "Tandrima Nandy", "Present"))
print()