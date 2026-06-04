n, p = map(int, input().split())
prices = list(map(int, input().split()))

prices.sort()

earnings = 0

for i in range(min(p, n)):
    if prices[i] < 0:
        earnings += -prices[i]
    else:
        break

print(earnings)