import sys

N = int(sys.stdin.readline())
count = 0

while True:
    if N % 5 == 0:
        count += N // 5
        print(count)
        break

    else:
        N -= 2
        count += 1

    if N < 0:
        print(-1)
        break