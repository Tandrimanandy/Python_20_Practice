'''
Question 1: Student Marks Analysis
A college stores students' marks in a list. Write a function that accepts a list of marks and displays the highest mark, 
lowest mark, average mark, and number of students who passed (marks of 40 or above).
'''

def analyze_marks(marks):
    if not marks:
        print("No marks to analyze.")
        return

    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)
    passed = sum(1 for mark in marks if mark >= 40)

    print(f"Highest mark: {highest}  \n Lowest mark: {lowest} \n Average mark: {average:.2f} \n Students passed: {passed}")


marks = [35, 72, 48, 90, 22, 60, 40, 55]
analyze_marks(marks)


