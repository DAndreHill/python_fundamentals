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
## Module 2 - Assignment 2

### Temperature Converter
File: temperature_converter.py
This program converts temperatures from Celsius to Fahrenheit using a temperature entered by the user.
Formula: Fahrenheit = (Celsius * 9 / 5) + 32
Test Result:
25 Celsius = 77.00 Fahrenheit (Passed)

### Simple Interest Calculator

File: simple_interest.py

This program calculates simple interest using the principal amount, interest rate, and time in years.

Formula: Simple Interest = (Principal * Rate * Time) / 100

Test Result:
Principal: $1000
Interest Rate: 5%
Time: 5 years
Simple Interest: $250.00 (Passed)

### First Ten U.S. Presidents
File: presidents.py

This program displays the first ten U.S. presidents and their terms in office using a for loop and a while loop.

The program uses an if/else statement to add an asterisk next to presidents whose last names begin with A.

Test Result:
Both loops displayed the first ten presidents and their terms successfully.
### How to Run Assignment 2

1. Open the project in VS Code.

2. Open the terminal.

3. Run the following programs individually:

python3 temperature_converter.py

python3 simple_interest.py

python3 presidents.py

4. Follow the instructions in the terminal.
   
