N = int(input())

count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if i == 3 or str(j).find("3") != -1 or str(k).find("3") != -1:
                count += 1
            k += 1
        j += 1
    i += 1

print(count)