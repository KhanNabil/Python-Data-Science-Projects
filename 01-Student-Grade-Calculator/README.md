# Student Grade Calculator

## Overview

This is my first Python practical project, where I built a simple Student Grade Calculator.

The program takes marks for multiple subjects as input, calculates the total marks and overall percentage, and assigns a grade based on the percentage. It also calculates the GPA and displays the highest and lowest marks.

While the program itself is fairly simple, the main goal was to understand how different Python concepts work together to solve a problem.

## Features

- Takes marks for any number of subjects from the user.
- Stores the marks in a Python list.
- Validates the input to ensure marks are between 0 and 100.
- Validates the number of subjects to ensure it is greater than zero.
- Calculates the total marks using Python's built-in `sum()` function.
- Calculates the overall percentage.
- Assigns a grade using conditional statements.
- Displays the highest and lowest marks using `max()` and `min()`.
- Calculates the GPA based on the average marks.

## Concepts Used

- Variables and data types
- Lists
- For loops
- While loops
- Nested loops
- Conditional statements (`if`, `elif`, `else`)
- Input validation
- Built-in functions (`sum()`, `max()`, `min()`)
- Basic mathematical calculations

## How It Works

The program first asks the user to enter the number of subjects. A `while` loop ensures that the number entered is greater than zero.

A `for` loop then handles the subjects, while a nested `while` loop ensures that invalid marks are not accepted. Marks must be between 0 and 100.

Once all the marks have been collected, the program calculates the total and percentage. It then uses conditional statements to determine the final grade.

The program also finds the highest and lowest marks and calculates the GPA using the average marks.

## Grading Criteria

| Percentage | Grade |
|---|---|
| 90–100% | A |
| 70–89% | B |
| 50–69% | C |
| 30–49% | D |
| Below 30% | Fail |

## How to Run

1. Make sure Python is installed on your system.
2. Clone or download this repository.
3. Open the project folder in your preferred IDE.
4. Run `main.py`.
5. Enter the number of subjects and marks when prompted.

## What I Learned

This practical helped me understand how loops, conditions and lists can work together in a single program.

One thing I particularly learned was how nested loops work. Initially, I struggled with understanding how a `while` loop could keep asking for input without moving to the next iteration of a `for` loop. Working through that helped me understand program execution and loop control much better.

I also learned how to validate user input, work with dynamic lists, and use built-in functions to perform calculations without writing everything from scratch.

## Future Improvements

- Allow multiple student records.
- Store student records in a database.
- Improve input handling to prevent errors when non-numeric values are entered.

---

**Author:** Khan Nabil  
**Course:** BSc Data Science  
**Project:** Python Practical 01
