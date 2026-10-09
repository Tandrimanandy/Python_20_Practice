# Python Questions and Answers 1 to 7

This repository contains Python solutions for the Python Lab Examination. Each question is written as a separate function, and each file calls its function to show the output. The project is ongoing, and more questions will be added.

## Status

| Section | Questions | Files | Status |
|---|---|---|---|
| Lists | 1 to 7 | q1.py, q2.py, q3.py, q4.py, 5th.py, 6th.py, q7.py | Completed |
| Tuples | 8 to 13 | Not yet added | Pending |
| Dictionaries | 14 to 20 | Not yet added | Pending |

## Functions Used in the Project

The table below lists every built-in function, list method, and custom function used in the seven files. Click a name to jump to its explanation further down this page.

| Function | Type | Used in | Why it is used |
|---|---|---|---|
| [max()](#max) | Built-in | q1.py, q2.py, 5th.py | Finds the highest value directly, without writing a loop. In 5th.py it is also used with index() to locate the top post. |
| [min()](#min) | Built-in | q1.py | Finds the lowest value directly. |
| [sum()](#sum) | Built-in | q1.py, q2.py, q4.py, 5th.py, q7.py | Adds all values together for totals and averages. |
| [len()](#len) | Built-in | q1.py, q3.py, q4.py, q7.py | Counts items, which is needed for averages and for the total product count. |
| [round()](#round) | Built-in | q4.py | Rounds each increased salary to two decimal places so currency values look correct. |
| [enumerate()](#enumerate) | Built-in | 5th.py, 6th.py, q7.py | Gives the index and the value together. The start=1 option produces human-friendly numbering such as Day 1 or Position 1. |
| [print()](#print) | Built-in | All files | Displays the results on the screen. |
| [input()](#input) | Built-in | 6th.py, q3.py | Reads values typed by the user, so the program can be tested with different data. |
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
| [List comprehension](#list-comprehension) | Concept | q1.py, q2.py, q4.py, 5th.py, q7.py | Builds filtered or transformed lists in one readable line instead of a multi-line loop. |
| [f-strings](#f-strings) | Concept | All files | Inserts variables into text and formats numbers, such as commas and two decimal places. |

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

`input()` reads text typed by the user while the program runs. It is used in 6th.py to enter a new patient's name and in q3.py to enter a new product. This makes the programs interactive and easy to test with different values.

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

## Concepts Used

### List comprehension

A list comprehension creates a new list by looping over an existing one in a single expression. For example, `[price for price in prices if price > 20000]` keeps only the expensive prices. It is used to make filtering and transforming lists shorter and easier to follow than a full loop with an `if` statement and an `append()` call.

### f-strings

An f-string places variables inside text by writing `f"..."` and putting the variable name in braces. The format options make numbers easier to read. For example, `{total_value:,}` adds thousand separators, and `{average:.2f}` shows two decimal places. Every file uses f-strings for its output.

## File Details

### q1.py

Solves Question 1, Student Marks Analysis. It uses `analyze_marks()` with a sample list of eight marks and prints the highest, lowest, and average marks, plus the number of students who passed.

### q2.py

Solves Question 2, Online Mobile Store. It uses `mob_store()` with a list of mobile prices and prints the expensive mobiles, the total inventory value, and the most expensive price.

### q3.py

Solves Question 3, Shopping Cart Management. It uses `manage_cart()` with a starting cart. The user enters a new product, the product "Shirt" is removed if it exists, and the final cart and total count are displayed.

### q4.py

Solves Question 4, Employee Salary Analysis. It uses `sal_analysis()` with a list of salaries and prints the average, the salaries above average, and the salaries after a 10% increase.

### 5th.py

Solves Question 5, Social Media Likes. It uses `soc_media_likes()` with a list of like counts and prints the top post, the total likes, and the posts with at least 100 likes.

### 6th.py

Solves Question 6, Hospital Patient Queue. It uses `update_queue()` with a starting queue. The first patient is served, the user enters a new patient's name, and the updated queue is displayed.

### q7.py

Solves Question 7, Daily Expense Tracker. It uses `expense_tracker()` with a list of daily expenses and prints the total, the daily average, and the days with spending above ₹1,000.

## How to Run

Requirements: Python 3.6 or later, because f-strings are used.

```bash
python q1.py
python q2.py
python q3.py
python q4.py
python 5th.py
python 6th.py
python q7.py
```

Files 3 and 6 ask for input when they run, so type a value and press Enter when prompted.

## Planned Work

- Add the tuple questions (Questions 8 to 13).
- Add the dictionary questions (Questions 14 to 20).
- Replace the sample data with values that the user can enter.
- Add a main menu that runs every question from one file.
