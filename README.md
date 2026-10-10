# : Python Based Codes :

This repository contains Python solutions for the Python Lab Examination. Each question is written as a separate function, and each file calls its function to show the output. The project is ongoing, and more questions will be added.

## Status

| Section | Questions | Files | Status |
|---|---|---|---|
| Lists | 1 to 7 | q1.py, q2.py, q3.py, q4.py, 5th.py, 6th.py, q7.py | Completed |
| Tuples | 8 to 13 | Section B_Tuple folder: q8.py, q9.py, q10, q11.py, q12.py | In progress |
| Dictionaries | 14 to 20 | Not yet added | Pending |

The Section B_Tuple folder is ongoing and not completed. Question 10 is still being checked, and Question 13 has not been written yet.

## Functions Used in the Project

The table below lists every built-in function, list method, tuple concept, and custom function used in the project files. Click a name to jump to its explanation further down this page.

| Function | Type | Used in | Why it is used |
|---|---|---|---|
| [max()](#max) | Built-in | q1.py, q2.py, 5th.py | Finds the highest value directly, without writing a loop. In 5th.py it is also used with index() to locate the top post. |
| [min()](#min) | Built-in | q1.py | Finds the lowest value directly. |
| [sum()](#sum) | Built-in | q1.py, q2.py, q4.py, 5th.py, q7.py | Adds all values together for totals and averages. |
| [len()](#len) | Built-in | q1.py, q3.py, q4.py, q7.py | Counts items, which is needed for averages and for the total product count. |
| [round()](#round) | Built-in | q4.py | Rounds each increased salary to two decimal places so currency values look correct. |
| [enumerate()](#enumerate) | Built-in | 5th.py, 6th.py, q7.py | Gives the index and the value together. The start=1 option produces human-friendly numbering such as Day 1 or Position 1. |
| [print()](#print) | Built-in | All files | Displays the results on the screen. |
| [input()](#input) | Built-in | 6th.py, q3.py, q12.py | Reads values typed by the user, so the program can be tested with different data. |
| [int()](#int) | Built-in | q12.py | Converts the text typed by the user into a whole number so that runs, balls, and boundaries can be used in calculations. |
| [list.append()](#listappend) | List method | 6th.py, q3.py | Adds a new item to the end of a list, such as a new patient or a new product. |
| [list.pop()](#listpop) | List method | 6th.py | Removes and returns the item at a given position. It removes the first patient after consultation. |
| [list.remove()](#listremove) | List method | q3.py | Removes the first matching item by value, such as a product that the customer no longer wants. |
| [list.index()](#listindex) | List method | 5th.py | Returns the position of a value, which identifies the post with the highest likes. |
| [analyze_marks()](#analyze_marks) | Custom | q1.py | Shows the highest, lowest, and average marks and counts the students who passed. |
| [mob_store()](#mob_store) | Custom | q2.py | Filters expensive mobiles, calculates inventory value, and finds the most expensive price. |
| [manage_cart()](#manage_cart) | Custom | q3.py | Adds a product, removes a product, and displays the final cart. |
| [sal_analysis()](#sal_analysis) | Custom | q4.py | Calculates the average salary, finds salaries above it, and applies a 10% increase. |
| [soc_media_likes()](#soc_media_likes) | Custom | 5th.py | Finds the top post, totals the likes, and lists posts with at least 100 likes. |
| [update_queue()](#update_queue) | Custom | 6th.py | Serves the first patient, adds a new patient, and displays the queue. |
| [expense_tracker()](#expense_tracker) | Custom | q7.py | Calculates total and average expenses and lists days above ₹1,000. |
| [student_record()](#student_record) | Custom | q8.py | Unpacks a student's tuple into separate fields, displays each field, and prints the full record. |
| [mobile_details()](#mobile_details) | Custom | q9.py | Unpacks a mobile's tuple, displays its details, and shows the price comparison with ₹30,000. |
| [order_details()](#order_details) | Custom | q11.py | Unpacks an order's tuple, calculates the total order value, and displays the order details. |
| [cricket_stats()](#cricket_stats) | Custom | q12.py | Calculates the strike rate and reports whether the player scored a half-century. |
| [List comprehension](#list-comprehension) | Concept | q1.py, q2.py, q4.py, 5th.py, q7.py | Builds filtered or transformed lists in one readable line instead of a multi-line loop. |
| [f-strings](#f-strings) | Concept | All files | Inserts variables into text and formats numbers, such as commas and two decimal places. |
| [Tuple unpacking](#tuple-unpacking) | Concept | q8.py, q9.py, q11.py, q12.py | Assigns each value in a tuple to its own variable in one line. |
| [Variable-length arguments](#variable-length-arguments) | Concept | q12.py | Lets a function accept any number of arguments, which is used here through *player. |
| [match-case](#match-case) | Concept | q12.py | Chooses the message for a century, a half-century, or neither, based on the runs scored. |

## Built-in Functions

### max()

`max()` returns the largest value in a sequence. It is used to find the highest mark in q1.py, the highest price in q2.py, and the highest like count in 5th.py. Using a built-in avoids writing a manual comparison loop, which makes the code shorter and less error-prone.

### min()

`min()` returns the smallest value in a sequence. It is used in q1.py to find the lowest mark. Like `max()`, it keeps the logic short and easy to read.

### sum()

`sum()` adds all the values in a sequence. It is used to calculate total inventory value in q2.py, average marks in q1.py, average salary in q4.py, total likes in 5th.py, and total expenses in q7.py. Almost every calculation in the project depends on it.

### len()

`len()` returns the number of items in a list. It is used to divide totals by counts for averages, and to count products in the shopping cart in q3.py. Using `len()` means the code works for any list size, not just the sample data.

### round()

`round()` rounds a number to a given number of decimal places. In q4.py it rounds each salary after the 10% increase to two decimal places, so the result looks like real currency values.

### enumerate()

`enumerate()` returns each item together with its position. It is used in 5th.py to label posts, in 6th.py to number the queue, and in q7.py to label days. The option `start=1` makes the numbering begin at 1 instead of 0, which matches how people normally count.

### print()

`print()` displays output on the screen. Every file uses it to show results, so the user can see what each function did.

### input()

`input()` reads text typed by the user while the program runs. It is used in 6th.py to enter a new patient's name, in q3.py to enter a new product, and in q12.py to enter a player's name, runs, balls, and boundaries. This makes the programs interactive and easy to test with different values.

### int()

`int()` converts text into a whole number. `input()` always returns text, so q12.py wraps the runs, balls, and boundaries inputs in `int()`. Without this conversion, the strike rate calculation would fail because text cannot be divided.

### list.append()

`append()` adds an item to the end of a list. It is used in q3.py to add a product to the cart and in 6th.py to add a new patient to the back of the queue. It changes the original list, which is what these programs need.

### list.pop()

`pop()` removes an item at a given index and returns it. In 6th.py, `pop(0)` removes the first patient in the queue, who has just finished consultation. The returned name is then used in the message shown to the user.

### list.remove()

`remove()` deletes the first item that matches a given value. In q3.py it removes a product the customer no longer wants. The function first checks that the item exists, which prevents an error when the product is missing.

### list.index()

`index()` returns the position of a value in a list. In 5th.py, `likes.index(max(likes))` finds the position of the highest like count, and adding 1 converts it to a post number that starts from 1.

## Custom Functions

### analyze_marks()

Defined in q1.py. It takes a list of marks and displays the highest mark, the lowest mark, the average mark, and the number of students who passed. It checks for an empty list first, so that dividing by zero cannot happen. Separating this logic into a function means it can be reused for any group of marks.

### mob_store()

Defined in q2.py. It takes a list of mobile prices, displays the mobiles costing more than ₹20,000, calculates the total inventory value, and shows the most expensive price. A list comprehension is used to filter the expensive mobiles.

### manage_cart()

Defined in q3.py. It accepts a cart list and optional add and remove values. It adds a product if one is given, removes a product if it exists, and then displays the final cart and the total count. Default values of `None` let the function be called with or without an add or remove action.

### sal_analysis()

Defined in q4.py. It calculates the average salary, lists the salaries above that average, and creates a new list with each salary increased by 10%. The function returns the increased salaries, so the result can be used by other parts of a program.

### soc_media_likes()

Defined in 5th.py. It finds the post with the highest likes, calculates the total likes, and lists the posts that received at least 100 likes. The function name is kept short and clear, and its output includes both post numbers and like counts.

### update_queue()

Defined in 6th.py. It removes the first patient from the queue, adds a new patient at the end, and displays the updated queue with positions. It checks whether the queue is empty before removing anyone, which prevents an error.

### expense_tracker()

Defined in q7.py. It calculates the total and average daily expenses and lists the days when spending went above ₹1,000. The days are numbered with `enumerate()` so the output is easy to read.

### student_record()

Defined in q8.py in the Section B_Tuple folder. It accepts a student record tuple containing the roll number, name, course, and semester. It unpacks the tuple into four variables, displays each field on its own line, and then prints the complete record. Tuples suit this data because a student's record is a fixed group of values that should not change after it is created.

### mobile_details()

Defined in q9.py in the Section B_Tuple folder. It accepts a mobile tuple containing the brand, model, price, and storage capacity. It unpacks the values, displays the details with the price formatted with thousand separators, and displays the comparison with ₹30,000. A tuple keeps each mobile's details together as one unit.

### order_details()

Defined in q11.py in the Section B_Tuple folder. It accepts an order tuple containing the order ID, product name, quantity, and unit price. It unpacks the tuple, multiplies the quantity by the unit price to find the total order value, and displays the order details. Storing an order as a tuple prevents accidental changes to a completed order.

### cricket_stats()

Defined in q12.py in the Section B_Tuple folder. It accepts a player's name, runs, balls, and boundaries, and calculates the strike rate using the formula (runs / balls) × 100. It uses a conditional expression to avoid dividing by zero when no balls were faced. A `match` statement then reports whether the player scored a century, a half-century, or neither. The function uses `*player`, so it can receive the player's details as separate arguments.

## Concepts Used

### List comprehension

A list comprehension creates a new list by looping over an existing one in a single expression. For example, `[price for price in prices if price > 20000]` keeps only the expensive prices. It is used to make filtering and transforming lists shorter and easier to follow than a full loop with an `if` statement and an `append()` call.

### f-strings

An f-string places variables inside text by writing `f"..."` and putting the variable name in braces. The format options make numbers easier to read. For example, `{total_value:,}` adds thousand separators, and `{average:.2f}` shows two decimal places. Every file uses f-strings for its output.

### Tuple unpacking

Tuple unpacking assigns each value in a tuple to a separate variable in one line. For example, `roll_no, name, course, semester = record` gives each field its own name. It is used in q8.py, q9.py, q11.py, and q12.py so that each value can be displayed or calculated easily.

### Variable-length arguments

Variable-length arguments allow a function to accept any number of values. In q12.py, `*player` collects the arguments into a tuple, and the function then unpacks that tuple into name, runs, balls, and boundaries. This keeps the function flexible while still using a tuple to hold the player's details.

### match-case

`match` and `case` compare a value against several patterns and run the first one that matches. In q12.py, the runs are checked against the century and half-century rules in order, and the last `case _` acts as the default. This is shorter and easier to read than a long chain of `if` and `elif` statements. It requires Python 3.10 or later.

## File Details

### Section B_Tuple folder

The files below are in the Section B_Tuple folder. This section covers the tuple questions and is ongoing, so it is not completed yet.

### q8.py

Solves Question 8, Student Registration Record. It uses `student_record()` with a sample tuple containing a roll number, name, course, and semester. It prints each field separately and then prints the complete record.

### q9.py

Solves Question 9, Mobile Product Details. It uses `mobile_details()` with a sample tuple containing the brand, model, price, and storage. It prints the details and displays the price comparison with ₹30,000.

### q10

Solves Question 10, GPS Location Tracking. This file is in progress. It is named `q10` without the `.py` extension, so rename it to `q10.py` before running it with Python. The question asks the program to display a delivery location's latitude and longitude and check whether they fall inside the approximate Kolkata bounding box of latitude 22.4 to 22.8 and longitude 88.2 to 88.5.

### q11.py

Solves Question 11, Product Order Details. It uses `order_details()` with a sample order tuple containing the order ID, product, quantity, and unit price. It prints the order details and the total order value.

### q12.py

Solves Question 12, Cricket Match Statistics. It uses `cricket_stats()` and asks the user to enter the player's name, runs, balls faced, and boundaries. It prints the details and the strike rate, then reports whether the player scored a century, a half-century, or neither.

### q7.py

Solves Question 7, Daily Expense Tracker. It uses `expense_tracker()` with a list of daily expenses and prints the total, the daily average, and the days with spending above ₹1,000.

## How to Run

Requirements: Python 3.10 or later is needed for q12.py because it uses match-case. The other files need Python 3.6 or later, because f-strings are used.

```bash
python q1.py
python q2.py
python q3.py
python q4.py
python 5th.py
python 6th.py
python q7.py
python "Section B_Tuple/q8.py"
python "Section B_Tuple/q9.py"
python "Section B_Tuple/q11.py"
python "Section B_Tuple/q12.py"
```

Files 3, 6, and 12 ask for input when they run, so type a value and press Enter when prompted.

## Planned Work

- Finish the Section B_Tuple folder: rename q10 to q10.py and confirm its output, then write Question 13 (Employee Attendance Record).
- Add the dictionary questions (Questions 14 to 20).
- Replace the sample data with values that the user can enter.
- Add a main menu that runs every question from one file.
