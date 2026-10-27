# Module 2 - Assignment 1
# Circle Area Calculator
# Calculates the area of a circle using a radius.

import math

print("Welcome to the Circle Area Calculator!")

while True:
    try:
        radius_input = input("Enter the radius: ").strip()

        if radius_input == "":
            print("Error: Please enter a radius.")
            continue

        radius = float(radius_input)

        if not math.isfinite(radius):
            print("Error: Enter a finite number.")
            continue

        if radius < 0:
            print("Error: Radius cannot be negative.")
            continue

        break

    except ValueError:
        print("Invalid input. Please enter a number.")

area = math.pi * radius ** 2

print(f"Radius: {radius_input.upper()}")
print(f"Characters entered: {len(radius_input)}")
print(f"Area of the circle: {area:.2f}")

