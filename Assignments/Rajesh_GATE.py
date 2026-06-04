n, x, y = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

low = a[y - 1]
high = a[y]

print(max(0, high - low - 1))