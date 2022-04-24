import sys

N, M, K = map(int, sys.stdin.readline().split())

list = []
for i in range(N):
    list.append(int(sys.stdin.readline()))

count = [0 for i in range(N)]
result = 0
num = 0
while any(list) == True:
        num = list.index(max(list))
        result += max(list)
        print(result)
        count[num] += 1
        if count[num] == 3:
            list[num] = 0

            continue

print(result)