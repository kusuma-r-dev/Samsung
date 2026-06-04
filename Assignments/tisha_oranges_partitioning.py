n = int(input())
orange = list(map(int, input().split()))

pivot = orange[n - 1]
x = 0

for i in range(n - 1):
    if orange[i] <= pivot:
        orange[i], orange[x] = orange[x], orange[i]
        x += 1

orange[x], orange[n - 1] = orange[n - 1], orange[x]

print(*orange)