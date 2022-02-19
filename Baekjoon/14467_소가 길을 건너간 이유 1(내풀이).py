n = int(input())

position = {}
count = 0

for i in range(n):
    position[i+1] = list()

for i in range(n):
    a, b = map(int , input().split())
    position[a].append(b)

for i in position:
    if not position[i]:
        continue
    else:
        start = position[i][0]
        for j in position[i]:
            if j != start:
                count += 1
            start = j

print(count)