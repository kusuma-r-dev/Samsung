def linearSearch(numbers, key):
    for i in range(len(numbers)):
        if numbers[i] == key:
            return i
    return -1


numbers = [10, 25, 30, 45, 50, 65]

print("List =", numbers)

key = int(input("Enter the element to search: "))

result = linearSearch(numbers, key)

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)