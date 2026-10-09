'''
Question 7: Daily Expense Tracker
A person records daily expenses in a list.
Write a function to calculate the total expenses, average daily expense, and the days on which expenses exceeded ₹1,000.
'''
def expense_tracker(expenses):
    total = sum(expenses)
    average = total / len(expenses)
    high_days = [f"Day {day}: ₹{amount}"
                 for day, amount in enumerate(expenses, start=1)
                 if amount > 1000]

    print(f"Total expenses: ₹{total} \n Average daily expense: ₹{average:.2f} \n Days with expenses above ₹1,000: ")

    for entry in high_days:  print(" ", entry)
expense_tracker([450, 1200, 800, 1500, 300, 1010, 670, 95])
print()