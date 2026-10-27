# Python Fundamentals
## Module 2 - Assignment 1

### Program Description
This Python program calculates the area of a circle
using a radius entered by the user.

### How to Run
1. Open the project in VS Code.
2. Open the Terminal.
3. Enter: python3 circle_area.py
4. Enter a radius when prompted.
5. The program displays the calculated area.

### Formula
Area = pi * radius ** 2

### Input Validation
The program checks for empty input, negative
numbers, invalid numeric values, and non-finite
numbers. Users can retry when an error occurs.

### String Manipulation
The program uses strip() to remove extra spaces,
upper() to transform the input, and len() to
count the characters entered.

### Exception Handling
The program uses try/except to handle ValueError
when a user enters invalid numeric input.

### Testing Results
- Radius 5: Area = 78.54 (Passed)
- Empty input: Error message displayed (Passed)
- Negative radius -5: Error message displayed (Passed)
- Retry with radius 5: Area = 78.54 (Passed)

### Edge Cases
An empty input and a negative radius were tested.
Both displayed an error and allowed another attempt.

### Assumptions
The radius must be a non-negative, finite number.
The calculated area is displayed to two decimal places.