'''
Question 4: Employee Salary Analysis
A company stores employee salaries in a list. Write a function to calculate the average salary,
 display salaries above the average, and increase every salary by 10%.
'''

def sal_analysis(salaries):
    average = sum(salaries) / len(salaries)
    above_average = [salary for salary in salaries if salary > average]
    increased = [round(salary * 1.10, 2) for salary in salaries]

    print(f"Average salary: ₹{average:,.2f} \n Salaries above average: {above_average} \n  Salaries after 10% increase: {increased}")
    return increased

sal_analysis([32000, 46000, 56000, 38000, 61000, 50000, 90000])
print()