#!/usr/bin/python3
# Importing functions from calculator_1.py
from calculator_1 import add, subtract, multiply, divide
a = 10
b = 5

result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)

print(f"Sum of {a} and {b} is: {result_add}")
print(f"Difference of {a} and {b} is: {result_subtract}")
print(f"Product of {a} and {b} is: {result_multiply}")
print(f"Division of {a} by {b} is: {result_divide}")

