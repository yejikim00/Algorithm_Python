student = []
for i in range(28):
    student.append(int(input()))

student = sorted(student)

check = [0] * 30
for i in student:
    check[i-1] = i

for j in check:
    if j == 0:
        print(check.index(j) + 1)
    check[check.index(j)] = -1