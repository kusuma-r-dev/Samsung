import sys
from partition import partition_list

numbers = [45,12,35,91,20]

print("Numbers before partition:\n", numbers)

partition_list(numbers, 0, len(numbers) - 1)

print("Numbers after partition:\n", numbers)