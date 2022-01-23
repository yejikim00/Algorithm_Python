N, M = map(int, input().split())

data = []
min_num = []
for i in range(N):
    data = list(map(int, input().split()))
    min_num.append(min(data))

print(max(min_num))