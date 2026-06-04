import sys
from quick_sort import quick_sort

numbers = [45,12,35,91,20]

print("Numbers before sorting:\n", numbers)

quick_sort(numbers, 0, len(numbers) - 1)

print("Numbers after sorting:\n", numbers)