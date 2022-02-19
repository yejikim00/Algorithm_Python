n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

res = 0
price = costs[0]

for i in range(n-1):
    if costs[i] < price:
        price = costs[i]
    res += price * roads[i]

print(res)