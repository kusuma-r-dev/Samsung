import sys
from factorial import find_factorial

input_number = int(input("Enter a number : "))

factorial_number = find_factorial(input_number)

print(f"Factorial of {input_number} is {factorial_number}")