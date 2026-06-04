t = int(input())

for _ in range(t):
    n = int(input())
    b = sorted(map(int, input().split()))
    g = sorted(map(int, input().split()))

    first = True
    for i in range(n):
        if b[i] > g[i] or (i < n - 1 and g[i] > b[i + 1]):
            first = False
            break

    second = True
    for i in range(n):
        if g[i] > b[i] or (i < n - 1 and b[i] > g[i + 1]):
            second = False
            break

    print("YES" if first or second else "NO")