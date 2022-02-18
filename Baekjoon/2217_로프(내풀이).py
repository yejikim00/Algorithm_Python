n = int(input())

loop = []
for i in range(n):
    loop.append(int(input()))

loop = sorted(loop)
result = []
for j in range(len(loop)):
    result.append(loop[0] * len(loop))
    loop.pop(0)

result = sorted(result)
print(result.pop())