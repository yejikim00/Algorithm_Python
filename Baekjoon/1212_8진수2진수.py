# 첫 번째 풀이
num_8 = list(map(int, input()))
num_8 = list(reversed(num_8))

num_10 = 0
for i in num_8:
    num_10 += i*(8**num_8.index(i))

num_2 = []
while True:
    if num_10 == 0:
        num_2.append(0)
        break
    num_2.append(num_10 % 2)
    num_10 = num_10 // 2
    if num_10 // 2 == 1:
        num_2.append(num_10 % 2)
        num_2.append(1)
        break

num_2 = reversed(num_2)

# 두 번째 풀이
num_8 = list(map(int, input()))
num_8 = list(reversed(num_8))

num_10 = 0
for i in num_8:
    num_10 += i * (8 ** num_8.index(i))

num_2 = bin(num_10)
print(int(num_2[2:]))

# 세 번째 풀이, 정답
print(bin(int(input(), 8))[2:])