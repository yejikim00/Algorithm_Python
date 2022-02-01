n, m = map(int, input().split())
dx, dy, d = map(int, input().split())

map_list = []
count = 0
for i in range(n):
    arr = map(int, input().split())
    map_list.append(list(arr))

step = [(0, -1), (-1, 0), (0, 1), (1, 0)]

for i in range(len(step)):
    if i == 0:
        dx += step[i][0]
        dy += step[i][1]
        count += 1
        break
    elif i == 1:
        dx += step[i][0]
        dy += step[i][1]
        count += 1
        break
    elif i == 2:
        dx += step[i][0]
        dy += step[i][1]
        count += 1
        break
    else:
        dx += step[i][0]
        dy += step[i][1]
        count += 1
        break
print(count)