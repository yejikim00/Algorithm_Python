t = int(input())

test = []
max_list = []
min_list = []
for i in range(t):
    n = int(input())
    test.append(list(map(int, input().split())))
    max_list.append(max(test[i]))
    min_list.append(min(test[i]))

for j in range(t):
    print(min_list[j], max_list[j])