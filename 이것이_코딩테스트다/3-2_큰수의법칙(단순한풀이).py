n, m, k = map(int, input().split())

list = list(map(int, input().split()))

list = sorted(list)
print(list)
data1 = list[-1]
data2 = list[-2]

result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += data1
        m -= 1
    if m == 0:
        break
    result += data2
    m -= 1

print(result)