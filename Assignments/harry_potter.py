n = int(input())
a = list(map(int, input().split()))
q, x = map(int, input().split())

stack = []
s = 0
idx = 0

for _ in range(q):
    op = input().strip()

    if op == "Harry":
        stack.append(a[idx])
        s += a[idx]
        idx += 1
    else:
        if stack:
            s -= stack.pop()

    if s == x:
        print(len(stack))
        break
else:
    print(-1)