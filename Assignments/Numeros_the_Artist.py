from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
brr = list(map(int, input().split()))

c1 = Counter(arr)
c2 = Counter(brr)

ans = []

for num in sorted(c2):
    if c2[num] > c1[num]:
        ans.append(num)

print(*ans)